import inspect
from collections.abc import Callable, Sequence
from enum import Enum, IntEnum
from functools import cached_property
from typing import Any, cast

from fastapi._compat import ModelField, lenient_issubclass
from fastapi.datastructures import Default, DefaultPlaceholder
from fastapi.dependencies.models import Dependant
from fastapi.dependencies.utils import (
    _get_body_field,
    _get_flat_body_params,
    _should_embed_body_fields,
    get_dependant,
    get_parameterless_sub_dependant,
    get_stream_item_type,
    get_typed_return_annotation,
)
from fastapi.responses import JSONResponse, Response
from fastapi.routing import _is_async_gen_callable, _is_gen_callable
from fastapi.sse import (
    EventSourceResponse,
    ServerSentEvent,
)
from fastapi.types import IncEx
from fastapi.utils import (
    create_model_field,
    generate_unique_id,
    get_value_or_default,
    is_body_allowed_for_status_code,
)

from fastapi import params, routing  # type: ignore[attr-defined]


def _add_cache_attribute(
    instance: routing._APIRouteLike, name: str, func: Callable[[Any], Any]
) -> None:
    cls = type(instance)

    if name in instance.__dict__ and (
        (val := instance.__dict__[name]) is None or val is False
    ):
        delattr(instance, name)

    # replace attribute with cached_property
    if not hasattr(cls, name) or not isinstance(getattr(cls, name), cached_property):
        prop = cached_property(func)
        setattr(cls, name, prop)
        prop.__set_name__(cls, name)


def _populate_api_route_state(
    route: routing._APIRouteLike,
    path: str,
    endpoint: Callable[..., Any],
    *,
    response_model: Any = Default(None),  # noqa: B008
    status_code: int | None = None,
    tags: list[str | Enum] | None = None,
    dependencies: Sequence[params.Depends] | None = None,
    summary: str | None = None,
    description: str | None = None,
    response_description: str = "Successful Response",
    responses: dict[int | str, dict[str, Any]] | None = None,
    deprecated: bool | None = None,
    name: str | None = None,
    methods: set[str] | list[str] | None = None,
    operation_id: str | None = None,
    response_model_include: IncEx | None = None,
    response_model_exclude: IncEx | None = None,
    response_model_by_alias: bool = True,
    response_model_exclude_unset: bool = False,
    response_model_exclude_defaults: bool = False,
    response_model_exclude_none: bool = False,
    include_in_schema: bool = True,
    response_class: type[Response] | DefaultPlaceholder = Default(JSONResponse),  # noqa: B008
    dependency_overrides_provider: Any | None = None,
    callbacks: list[routing.BaseRoute] | None = None,
    openapi_extra: dict[str, Any] | None = None,
    generate_unique_id_function: Callable[[Any], str] | DefaultPlaceholder = Default(  # noqa: B008
        generate_unique_id
    ),
    strict_content_type: bool | DefaultPlaceholder = Default(True),  # noqa: B008
    stream_item_type: Any | None = None,
) -> None:
    route.path = path
    route.endpoint = endpoint
    route.stream_item_type = stream_item_type

    route.summary = summary
    route.response_description = response_description
    route.deprecated = deprecated
    route.operation_id = operation_id
    route.response_model_include = response_model_include
    route.response_model_exclude = response_model_exclude
    route.response_model_by_alias = response_model_by_alias
    route.response_model_exclude_unset = response_model_exclude_unset
    route.response_model_exclude_defaults = response_model_exclude_defaults
    route.response_model_exclude_none = response_model_exclude_none
    route.include_in_schema = include_in_schema
    route.response_class = response_class
    route.dependency_overrides_provider = dependency_overrides_provider
    route.callbacks = callbacks
    route.openapi_extra = openapi_extra
    route.generate_unique_id_function = generate_unique_id_function
    route.strict_content_type = strict_content_type
    route.tags = tags or []
    route.responses = responses or {}
    route.name = routing.get_name(endpoint) if name is None else name
    route.path_regex, route.path_format, route.param_convertors = routing.compile_path(
        path
    )
    if methods is None:
        methods = ["GET"]
    route.methods = {method.upper() for method in methods}
    if isinstance(generate_unique_id_function, DefaultPlaceholder):
        current_generate_unique_id: Callable[[Any], str] = (
            generate_unique_id_function.value
        )
    else:
        current_generate_unique_id = generate_unique_id_function
    route.unique_id = route.operation_id or current_generate_unique_id(route)
    # normalize enums e.g. http.HTTPStatus
    if isinstance(status_code, IntEnum):
        status_code = int(status_code)
    route.status_code = status_code

    # Store the raw response_model / stream_item_type parameters so the
    # deferred cached_properties can access them per-instance (not via
    # closure, which would be shared across all instances of the class).
    route._raw_response_model = response_model  # ty: ignore[unresolved-attribute]
    route._raw_stream_item_type = stream_item_type  # ty: ignore[unresolved-attribute]

    def _response_field(self):
        if self.response_model:
            assert is_body_allowed_for_status_code(self.status_code), (
                f"Status code {self.status_code} must not have a response body"
            )
            response_name = "Response_" + self.unique_id
            return create_model_field(
                name=response_name,
                type_=self.response_model,
                mode="serialization",
            )
        else:
            return None

    _add_cache_attribute(route, "response_field", _response_field)

    def _stream_item_field(self) -> ModelField | None:
        if not self.stream_item_type:
            return None
        stream_item_name = "StreamItem_" + self.unique_id
        return create_model_field(
            name=stream_item_name,
            type_=self.stream_item_type,
            mode="serialization",
        )

    _add_cache_attribute(route, "stream_item_field", _stream_item_field)

    route.dependencies = list(dependencies or [])
    route.description = description or inspect.cleandoc(route.endpoint.__doc__ or "")
    # if a "form feed" character (page break) is found in the description text,
    # truncate description text to the content preceding the first "form feed"
    route.description = route.description.split("\f")[0].strip()

    def _response_fields(self) -> dict[int | str, ModelField]:
        response_fields: dict[int | str, ModelField] = {}
        for additional_status_code, response in self.responses.items():
            assert isinstance(response, dict), "An additional response must be a dict"
            model = response.get("model")
            if model:
                assert is_body_allowed_for_status_code(additional_status_code), (
                    f"Status code {additional_status_code} must not have a response body"
                )
                response_name = f"Response_{additional_status_code}_{self.unique_id}"
                response_field = create_model_field(
                    name=response_name, type_=model, mode="serialization"
                )
                response_fields[additional_status_code] = response_field
        return response_fields

    _add_cache_attribute(route, "response_fields", _response_fields)

    assert callable(endpoint), "An endpoint must be a callable"

    def _get_dependant(self: routing._APIRouteLike) -> Dependant:
        dependant = get_dependant(
            path=self.path_format, call=self.endpoint, scope="function"
        )

        for depends in self.dependencies[::-1]:
            dependant.dependencies.insert(
                0,
                get_parameterless_sub_dependant(depends=depends, path=self.path_format),
            )

        return dependant

    _add_cache_attribute(route, "dependant", _get_dependant)

    def _flat_body_params(self) -> list[ModelField]:
        return _get_flat_body_params(self.dependant)

    _add_cache_attribute(route, "_flat_body_params", _flat_body_params)

    def _embed_body_fields(self):
        return _should_embed_body_fields(self._flat_body_params)

    _add_cache_attribute(route, "_embed_body_fields", _embed_body_fields)

    def _body_field(self):
        return _get_body_field(
            name=self.unique_id,
            body_params=self._flat_body_params,
            embed_body_fields=self._embed_body_fields,
        )

    _add_cache_attribute(route, "body_field", _body_field)

    # Detect generator endpoints that should stream as JSONL or SSE
    def _is_generator(self) -> bool:
        return _is_async_gen_callable(self.dependant.call) or _is_gen_callable(
            self.dependant.call
        )

    _add_cache_attribute(route, "is_generator", _is_generator)

    def _is_sse_stream(self) -> bool:
        return self.is_generator and lenient_issubclass(
            self.response_class, EventSourceResponse
        )

    _add_cache_attribute(route, "is_sse_stream", _is_sse_stream)

    def _is_json_stream(self) -> bool:
        return self.is_generator and isinstance(self.response_class, DefaultPlaceholder)

    _add_cache_attribute(route, "is_json_stream", _is_json_stream)

    def _resolved_response_model_stream_item(self):
        resolved_model = self._raw_response_model
        resolved_item_type = self._raw_stream_item_type
        if isinstance(resolved_model, DefaultPlaceholder):
            return_annotation = get_typed_return_annotation(self.endpoint)
            if lenient_issubclass(return_annotation, Response):
                resolved_model = None
            else:
                stream_item = get_stream_item_type(return_annotation)
                if stream_item is not None and self.is_generator:
                    # Extract item type for JSONL or SSE streaming for
                    # generator endpoints when response_class is
                    # DefaultPlaceholder (JSONL) or EventSourceResponse (SSE).
                    # ServerSentEvent is excluded: it's a transport
                    # wrapper, not a data model, so it shouldn't feed
                    # into validation or OpenAPI schema generation.
                    if (
                        isinstance(self.response_class, DefaultPlaceholder)
                        or lenient_issubclass(self.response_class, EventSourceResponse)
                    ) and not lenient_issubclass(stream_item, ServerSentEvent):
                        resolved_item_type = stream_item
                    resolved_model = None
                else:
                    resolved_model = return_annotation

        return resolved_model, resolved_item_type

    _add_cache_attribute(
        route,
        "_resolved_response_model_stream_item",
        _resolved_response_model_stream_item,
    )

    def _response_model(self):

        return self._resolved_response_model_stream_item[0]

    _add_cache_attribute(route, "response_model", _response_model)

    def _stream_item_type(self):
        return self._resolved_response_model_stream_item[1]

    _add_cache_attribute(route, "stream_item_type", _stream_item_type)


class DeferringAPIRoute(routing.APIRoute):
    def __init__(
        self, path: str, endpoint: Callable[..., Any], *args, **kwargs
    ) -> None:
        _populate_api_route_state(
            cast(routing._APIRouteLike, self), path, endpoint, *args, **kwargs
        )

    @cached_property
    def app(self):
        return routing.request_response(self.get_route_handler())


class DeferringAPIRouter(routing.APIRouter):
    def __init__(self, *args, **kwargs):
        if "route_class" not in kwargs:
            kwargs["route_class"] = DeferringAPIRoute
        super().__init__(*args, **kwargs)


def _from_api_route_deferred(
    cls: type, *, original_route: Any, include_context: Any
) -> Any:
    """Deferring replacement for fastapi>=0.162's `_EffectiveRouteContext.from_api_route`.

    Upstream eagerly builds the ASGI app for every route of an included router
    (`context.app = request_response(original_route.get_route_handler())`),
    which forces the deferred dependant/body_field/response_model to be
    computed at include time. Defer `app` to first access instead, like
    DeferringAPIRoute does for direct routes.
    """
    route = cast(routing._APIRouteLike, original_route)
    context = cls(original_route=original_route)
    _populate_api_route_state(
        cast(routing._APIRouteLike, context),
        include_context.path_for(original_route),
        route.endpoint,
        response_model=route.response_model,
        status_code=route.status_code,
        tags=[*include_context.tags, *route.tags],
        dependencies=[*include_context.dependencies, *route.dependencies],
        summary=route.summary,
        description=route.description,
        response_description=route.response_description,
        responses={**include_context.responses, **route.responses},
        deprecated=route.deprecated or include_context.deprecated,
        methods=route.methods,
        operation_id=route.operation_id,
        response_model_include=route.response_model_include,
        response_model_exclude=route.response_model_exclude,
        response_model_by_alias=route.response_model_by_alias,
        response_model_exclude_unset=route.response_model_exclude_unset,
        response_model_exclude_defaults=route.response_model_exclude_defaults,
        response_model_exclude_none=route.response_model_exclude_none,
        include_in_schema=route.include_in_schema and include_context.include_in_schema,
        response_class=get_value_or_default(
            route.response_class,
            include_context.included_router.default_response_class,
            include_context.default_response_class,
        ),
        name=route.name,
        dependency_overrides_provider=include_context.dependency_overrides_provider,
        callbacks=[*include_context.callbacks, *(route.callbacks or [])],
        openapi_extra=route.openapi_extra,
        generate_unique_id_function=get_value_or_default(
            route.generate_unique_id_function,
            include_context.included_router.generate_unique_id_function,
            include_context.generate_unique_id_function,
        ),
        strict_content_type=get_value_or_default(
            route.strict_content_type,
            include_context.included_router.strict_content_type,
            include_context.strict_content_type,
        ),
        stream_item_type=route.stream_item_type,
    )

    def _app(self: Any) -> Any:
        # Build the handler lazily with the effective context active, mirroring
        # upstream's ContextVar usage so integrations wrapping dependant.call
        # while constructing the handler still see the context.
        context_var = getattr(routing, "_effective_route_context_var", None)
        if context_var is not None:
            token = context_var.set(self)
            try:
                handler = self.original_route.get_route_handler()
            finally:
                context_var.reset(token)
        else:
            handler = self.original_route.get_route_handler()
        return routing.request_response(handler)

    _add_cache_attribute(context, "app", _app)
    return context


def apply_include_patch(routing_module: Any) -> bool:
    """Patch fastapi>=0.162's include machinery to defer app construction.

    Returns True when the patch was applied, i.e. the running fastapi version
    has `_EffectiveRouteContext` (older versions re-run APIRoute.__init__ on
    include, which the route-class patch already covers).
    """
    effective_route_context = getattr(routing_module, "_EffectiveRouteContext", None)
    if effective_route_context is None:
        return False
    effective_route_context.from_api_route = classmethod(_from_api_route_deferred)
    return True
