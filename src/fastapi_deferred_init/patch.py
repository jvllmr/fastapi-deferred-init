from .routing import _populate_api_route_state


def apply_patch() -> None:
    from fastapi import routing  # type: ignore[attr-defined]

    routing._populate_api_route_state = _populate_api_route_state
