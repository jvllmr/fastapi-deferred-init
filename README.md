# fastapi-deferred-init


## The Problem

When using nested routers in a FastAPI project its start-up time can get long quite fast.
That is because every router re-calculates the routes defined by a nested router when including it and the pre-calculated values by the nested router never get used. In short: values in nested routers are calculated although they will never be used.

## The Solution

This library provides a modified APIRoute that defers the calculation of values to the first actual attribute access. A router which uses the route as a default is also provided.

## Caveat
When using the deferred APIRoute on every layer of the app, startup errors are deferred to the first time a route is called. So errors related to route registration might go undetected if the route is not tested at least once.
