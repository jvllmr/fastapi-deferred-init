import os

import pytest
from pydantic import BaseModel

from fastapi import APIRouter, FastAPI
from fastapi.routing import iter_route_contexts
from fastapi.testclient import TestClient
from fastapi_deferred_init.routing import _populate_api_route_state

from .data.gen_code_ast import create_code
from .helpers import import_via_file_path, load_code


def skip_test(use_lib: bool):
    if not use_lib and not os.getenv("FULL_TEST"):
        pytest.skip()


@pytest.mark.parametrize(["use_lib"], [(True,), (False,)])
def test_basic(use_lib: bool, benchmark, monkeypatch):
    skip_test(use_lib=use_lib)
    if use_lib:
        monkeypatch.setattr(
            "fastapi.routing._populate_api_route_state", _populate_api_route_state
        )
    create_code(
        50,
    )

    generated_code = benchmark(load_code)

    app = FastAPI()
    router = generated_code.router

    app.include_router(router)

    client = TestClient(app)
    routes = list(iter_route_contexts(app.routes))
    assert len(routes) == 54
    for route in routes:
        resp = client.get(route.path)
        assert resp.status_code == 200


@pytest.mark.parametrize(["use_lib"], [(True,), (False,)])
def test_with_pydantic_model(use_lib: bool, monkeypatch):
    skip_test(use_lib=use_lib)
    if use_lib:
        monkeypatch.setattr(
            "fastapi.routing._populate_api_route_state", _populate_api_route_state
        )
    app = FastAPI()
    router = APIRouter()

    class Login(BaseModel):
        username: str
        password: str

    @router.post("/login")
    async def do_login(json: Login):
        assert isinstance(json, Login)
        assert isinstance(json.username, str)
        assert isinstance(json.password, str)

        return {"userdata": "[...]"}

    app.include_router(router)

    client = TestClient(app)

    resp = client.post("/login", json={"username": "jvllmr", "password": "password"})
    assert resp.status_code == 200


def test_fastapi_openapi_schema(monkeypatch):
    monkeypatch.setattr(
        "fastapi.routing._populate_api_route_state", _populate_api_route_state
    )

    import_via_file_path(
        "fastapi_clone.tests.test_additional_properties",
        "fastapi/tests/test_additional_properties.py",
    )

    import_via_file_path(
        "fastapi_clone.tests.test_openapi_examples",
        "fastapi/tests/test_openapi_examples.py",
    )

    from fastapi_clone.tests.test_additional_properties import (  # noqa # type: ignore
        test_openapi_schema as fastapi_test_openapi_schema_additional,
    )
    from fastapi_clone.tests.test_openapi_examples import (  # noqa # type: ignore
        test_openapi_schema as fastapi_test_openapi_schema,
    )

    fastapi_test_openapi_schema()
    fastapi_test_openapi_schema_additional()


def test_fastapi_sse(monkeypatch):
    monkeypatch.setattr(
        "fastapi.routing._populate_api_route_state", _populate_api_route_state
    )
    import_via_file_path(
        "fastapi_clone.tests.test_sse",
        "fastapi/tests/test_sse.py",
    )

    from fastapi_clone.tests.test_sse import (  # type: ignore
        test_raw_data_sent_without_json_encoding as fastapi_test_raw_data_sent_without_json_encoding,
        client_fixture as fastapi_client_fixture,
    )

    for client in fastapi_client_fixture.__wrapped__():
        fastapi_test_raw_data_sent_without_json_encoding(client)
