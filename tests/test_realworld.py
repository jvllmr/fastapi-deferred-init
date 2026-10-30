"""Real-world usage tests for fastapi-deferred-init.

These tests mimic common patterns found in production FastAPI apps
that go beyond what the existing tests cover.
"""

import typing as t

from fastapi.responses import JSONResponse, PlainTextResponse
from fastapi.testclient import TestClient
from pydantic import BaseModel

from fastapi import Depends, FastAPI, Header, HTTPException, Query, routing, status

from .helpers import apply_monkeypatch


class User(BaseModel):
    id: int
    name: str
    email: str


class Item(BaseModel):
    id: int
    title: str
    owner_id: int


def _make_app():
    """Build a realistic app. Route creation order matters: router routes
    are created before app-level routes because decorators run top-to-bottom."""

    def get_current_user() -> str:
        return "fake-token"

    def get_db() -> str:
        return "fake-db-conn"

    # --- sub-router: items (created FIRST, so its closures get installed on the class) ---
    items_router = routing.APIRouter(prefix="/items", tags=["items"])

    @items_router.get("/{item_id}", response_model=Item)
    def read_item(item_id: int, db: t.Annotated[str, Depends(get_db)]):
        return Item(id=item_id, title=f"Item {item_id}", owner_id=1)

    @items_router.post("", response_model=Item, status_code=status.HTTP_201_CREATED)
    def create_item(item: Item, user: t.Annotated[str, Depends(get_current_user)]):
        return item

    # --- sub-router: users ---
    users_router = routing.APIRouter(prefix="/users", tags=["users"])

    @users_router.get("/{user_id}", response_model=User)
    def read_user(user_id: int):
        if user_id == 999:
            raise HTTPException(status_code=404, detail="User not found")
        return User(
            id=user_id, name=f"User {user_id}", email=f"user{user_id}@example.com"
        )

    # --- v1 router ---
    v1_router = routing.APIRouter(prefix="/v1")
    v1_router.include_router(items_router)
    v1_router.include_router(users_router, prefix="/u", tags=["v1-users"])

    # --- app (created LAST) ---
    app = FastAPI(title="Real World App")

    @app.get("/", response_class=PlainTextResponse)
    def root():
        return "Hello World"

    @app.get("/health")
    def health():
        return {"status": "ok"}

    app.include_router(v1_router)
    return app


def test_nested_routers_with_response_model_and_dependencies(monkeypatch):
    apply_monkeypatch(monkeypatch)
    app = _make_app()
    client = TestClient(app)

    # Direct app routes
    resp = client.get("/")
    assert resp.status_code == 200, resp.text
    assert resp.text == "Hello World"

    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.json() == {"status": "ok"}

    # Nested router routes
    resp = client.get("/v1/items/42")
    assert resp.status_code == 200, resp.text
    assert resp.json() == {"id": 42, "title": "Item 42", "owner_id": 1}

    resp = client.post("/v1/items", json={"id": 1, "title": "Test", "owner_id": 2})
    assert resp.status_code == 201, resp.text
    assert resp.json() == {"id": 1, "title": "Test", "owner_id": 2}

    resp = client.get("/v1/u/users/5")
    assert resp.status_code == 200, resp.text
    assert resp.json() == {"id": 5, "name": "User 5", "email": "user5@example.com"}

    resp = client.get("/v1/u/users/999")
    assert resp.status_code == 404, resp.text

    # OpenAPI schema should be generatable
    resp = client.get("/openapi.json")
    assert resp.status_code == 200, resp.text
    schema = resp.json()
    assert "/v1/items/{item_id}" in schema["paths"]
    assert "/v1/u/users/{user_id}" in schema["paths"]
    assert "/" in schema["paths"]


def test_response_model_not_leaked_between_routes(monkeypatch):
    """Regression test: response_model from one route must not leak to another.

    The deferred cached_property closures were installed once per class,
    capturing the first route's parameters for all subsequent routes.
    """
    apply_monkeypatch(monkeypatch)

    # First route with response_model — its closures get installed on the class
    router_a = routing.APIRouter()

    @router_a.get("/a", response_model=Item)
    def get_a():
        return Item(id=1, title="A", owner_id=0)

    # Second route WITHOUT response_model — should NOT inherit Item
    router_b = routing.APIRouter()

    @router_b.get("/b")
    def get_b():
        return {"plain": "dict"}

    app = FastAPI()
    app.include_router(router_a)
    app.include_router(router_b)

    # Check the original routes' response_model
    for r in router_b.routes:
        assert r.response_model is None, (  # ty: ignore[unresolved-attribute]
            f"Route {r.path} incorrectly has response_model={r.response_model} "  # ty: ignore[unresolved-attribute]
            f"(leaked from another route)"
        )

    client = TestClient(app)
    resp = client.get("/b")
    assert resp.status_code == 200, resp.text
    assert resp.json() == {"plain": "dict"}

    # Also verify /a still works
    resp = client.get("/a")
    assert resp.status_code == 200, resp.text
    assert resp.json() == {"id": 1, "title": "A", "owner_id": 0}


def test_custom_response_class_not_leaked(monkeypatch):
    """Custom response_class on one route must not leak to others."""
    apply_monkeypatch(monkeypatch)

    router = routing.APIRouter()

    @router.get("/html", response_class=PlainTextResponse)
    def html():
        return "<h1>hi</h1>"

    @router.get("/json")
    def json_route():
        return {"ok": True}

    app = FastAPI()
    app.include_router(router)

    client = TestClient(app)
    resp = client.get("/html")
    assert resp.status_code == 200
    assert "text/plain" in resp.headers["content-type"]

    resp = client.get("/json")
    assert resp.status_code == 200
    assert "application/json" in resp.headers["content-type"]
    assert resp.json() == {"ok": True}


def test_dependency_overrides(monkeypatch):
    apply_monkeypatch(monkeypatch)

    def original_dep():
        return "original"

    def override_dep():
        return "overridden"

    router = routing.APIRouter()

    @router.get("/dep")
    def get_dep(val: t.Annotated[str, Depends(original_dep)]):
        return {"val": val}

    app = FastAPI()
    app.include_router(router)
    app.dependency_overrides[original_dep] = override_dep

    client = TestClient(app)
    resp = client.get("/dep")
    assert resp.status_code == 200, resp.text
    assert resp.json() == {"val": "overridden"}


def test_multiple_includes_same_router(monkeypatch):
    apply_monkeypatch(monkeypatch)

    router = routing.APIRouter()

    @router.get("/ping")
    def ping():
        return {"pong": True}

    app = FastAPI()
    app.include_router(router, prefix="/api/v1")
    app.include_router(router, prefix="/api/v2")

    client = TestClient(app)
    for prefix in ("/api/v1", "/api/v2"):
        resp = client.get(f"{prefix}/ping")
        assert resp.status_code == 200, f"{prefix}: {resp.text}"
        assert resp.json() == {"pong": True}


def test_path_and_query_params(monkeypatch):
    apply_monkeypatch(monkeypatch)

    router = routing.APIRouter(prefix="/search")

    @router.get("/{category}")
    def search(
        category: str,
        q: str = Query(default=""),
        limit: int = Query(default=10, le=100),
        x_token: str = Header(default=""),
    ):
        return {"category": category, "q": q, "limit": limit, "token": x_token}

    app = FastAPI()
    app.include_router(router)

    client = TestClient(app)
    resp = client.get("/search/books?q=fastapi&limit=5", headers={"X-Token": "abc"})
    assert resp.status_code == 200, resp.text
    assert resp.json() == {
        "category": "books",
        "q": "fastapi",
        "limit": 5,
        "token": "abc",
    }


def test_head_returns_405_like_upstream(monkeypatch):
    """HEAD on a GET-only route returns 405 — same as unpatched FastAPI."""
    apply_monkeypatch(monkeypatch)

    router = routing.APIRouter()

    @router.get("/auto")
    def auto():
        return {"ok": True}

    app = FastAPI()
    app.include_router(router)

    client = TestClient(app)
    resp = client.head("/auto")
    assert resp.status_code == 405, resp.text


def test_exception_handlers(monkeypatch):
    apply_monkeypatch(monkeypatch)

    router = routing.APIRouter()

    class CustomError(Exception):
        pass

    @router.get("/custom-error")
    def raise_custom():
        raise CustomError("something went wrong")

    @router.get("/validation-error")
    def cause_validation(q: int):
        return {"q": q}

    app = FastAPI()

    @app.exception_handler(CustomError)
    def custom_handler(request, exc):
        return JSONResponse(status_code=418, content={"error": str(exc)})

    app.include_router(router)

    client = TestClient(app)
    resp = client.get("/custom-error")
    assert resp.status_code == 418, resp.text
    assert resp.json() == {"error": "something went wrong"}

    resp = client.get("/validation-error?q=notanint")
    assert resp.status_code == 422, resp.text
