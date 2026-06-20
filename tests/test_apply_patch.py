from fastapi_deferred_init.routing import (
    DeferringAPIRouter,
    _populate_api_route_state,
    DeferringAPIRoute,
)


def test_if_patch_applied():
    from .patched_app import app

    assert isinstance(app.router, DeferringAPIRouter), type(app.router)

    from fastapi import routing

    assert routing.APIRouter is DeferringAPIRouter
    assert routing.APIRoute is DeferringAPIRoute
    assert routing._populate_api_route_state is _populate_api_route_state
