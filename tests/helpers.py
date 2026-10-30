from __future__ import annotations

import importlib
import importlib.util
import sys
from contextlib import contextmanager
from cProfile import Profile
from pstats import SortKey, Stats
from typing import TYPE_CHECKING

from fastapi_deferred_init.routing import (
    DeferringAPIRoute,
    DeferringAPIRouter,
    _from_api_route_deferred,
    _populate_api_route_state,
)

if TYPE_CHECKING:
    import pytest


@contextmanager
def profiled():
    with Profile() as profiler:
        yield
        stats = Stats(profiler)
        stats.sort_stats(SortKey.CUMULATIVE)
        stats.print_stats()
        stats.dump_stats("profile")


def load_code():
    if "tests.data.code" in sys.modules:
        del sys.modules["tests.data.code"]
    return importlib.import_module("tests.data.code")


def import_via_file_path(module_name: str, file_path: str):
    # https://docs.python.org/3/library/importlib.html#importing-a-source-file-directly
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)


def apply_monkeypatch(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(
        "fastapi.routing._populate_api_route_state", _populate_api_route_state
    )
    monkeypatch.setattr("fastapi.routing.APIRoute", DeferringAPIRoute)
    monkeypatch.setattr("fastapi.routing.APIRouter", DeferringAPIRouter)
    monkeypatch.setattr("fastapi.APIRouter", DeferringAPIRouter)
    monkeypatch.setattr(
        "fastapi.routing._EffectiveRouteContext.from_api_route",
        classmethod(_from_api_route_deferred),
        raising=False,
    )
