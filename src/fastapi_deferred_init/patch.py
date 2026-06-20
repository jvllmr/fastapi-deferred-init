from .routing import _populate_api_route_state, DeferringAPIRoute, DeferringAPIRouter


def apply_patch() -> None:

    from fastapi import routing  # type: ignore[attr-defined]

    routing._populate_api_route_state = _populate_api_route_state  # ty:ignore[invalid-assignment]
    routing.APIRoute = DeferringAPIRoute  # ty:ignore[invalid-assignment]
    routing.APIRouter = DeferringAPIRouter
