from .routing import (
    DeferringAPIRoute,
    DeferringAPIRouter,
    _populate_api_route_state,
    apply_include_patch,
)


def apply_patch() -> None:

    from fastapi import routing  # type: ignore[attr-defined]

    routing._populate_api_route_state = _populate_api_route_state  # ty:ignore[invalid-assignment]
    routing.APIRoute = DeferringAPIRoute  # ty:ignore[invalid-assignment]
    routing.APIRouter = DeferringAPIRouter  # ty:ignore[invalid-assignment]
    apply_include_patch(routing)

    import fastapi

    fastapi.APIRouter = DeferringAPIRouter  # type:ignore[attr-defined]  # ty:ignore[invalid-assignment]
