# fastapi-deferred-init

![PyPI - Downloads](https://img.shields.io/pypi/dd/fastapi-deferred-init)
[![GitHub license](https://img.shields.io/github/license/jvllmr/fastapi-deferred-init)](https://github.com/jvllmr/fastapi-deferred-init/blob/master/LICENSE)
![Tests](https://github.com/jvllmr/fastapi-deferred-init/actions/workflows/test.yml/badge.svg)

## The Problem

When using nested routers in a FastAPI project its start-up time can get long quite fast.
That is because every router re-calculates the routes defined by a nested router when including it and the pre-calculated values by the nested router never get used. In short: values in nested routers are calculated although they will never be used.

## The Solution

This library provides a modified APIRoute that defers the calculation of values to the first actual attribute access. A router which uses the route as a default is also provided.

## Usage

Older versions of this library worked by simply using custom APIRoute and APIRouter classes, but since FastAPI version 0.137.0 the optimizations require monkey patching to take effect. The following example shows how the patches can be applied by creating an `asgi.py` file as your entrypoint:

```python
# my_app/asgi.py
from fastapi_deferred_init import apply_patch

# important! don't import anything else before this to make sure the patch works as expected
apply_patch()

# run your app with i.e. gunicorn my_app.asgi:app
from my_app.app import app

# mark app as re-export
__all__ = ["app"]
```

## Caveat

When using the deferred APIRoute on every layer of the app, startup errors are deferred to the first time a route is called. So errors related to route registration might go undetected if the route is not tested at least once.

## Pull Request

I created a pull request to merge this change back into FastAPI: https://github.com/tiangolo/fastapi/pull/10589
It was closed since major refactors to FastAPI are underway, but I might re-open it once the maintainers are ready.
