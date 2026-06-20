from fastapi.dependencies.models import Dependant
import inspect
from enum import Enum, IntEnum
from functools import cached_property
from typing import Any, Callable, Union, cast
from collections.abc import Sequence


from fastapi.sse import (
    EventSourceResponse,
    ServerSentEvent,
)
from fastapi import params, routing  # type: ignore[attr-defined]
from fastapi._compat import ModelField, lenient_issubclass
from fastapi.datastructures import Default, DefaultPlaceholder
from fastapi.dependencies.utils import (
    _should_embed_body_fields,
    get_body_field,
    get_dependant,
    get_flat_dependant,
    get_parameterless_sub_dependant,
    get_typed_return_annotation,
    get_stream_item_type,
)
from fastapi.responses import JSONResponse, Response
from fastapi.types import IncEx
from fastapi.utils import (
    create_model_field,
    generate_unique_id,
    is_body_allowed_for_status_code,
)


def _add_cache_attribute(
    instance: routing._APIRouteLike, name: str, func: Callable[[Any], Any]
) -> None:
    cls = type(instance)
    if hasattr(instance, name) and (
        (val := getattr(instance, name)) is None or val is False
    ):
        delattr(instance, name)

    if not hasattr(cls, name) or not isinstance(getattr(cls, name), cached_property):
        prop = cached_property(func)
        setattr(cls, name, prop)
        prop.__set_name__(cls, name)


def _populate_api_route_state(
    route: routing._APIRouteLike,
    path: str,
    endpoint: Callable[..., Any],
    *,
    response_model: Any = Default(None),
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
    response_class: type[Response] | DefaultPlaceholder = Default(JSONResponse),
    dependency_overrides_provider: Any | None = None,
    callbacks: list[routing.BaseRoute] | None = None,
    openapi_extra: dict[str, Any] | None = None,
    generate_unique_id_function: Callable[[Any], str] | DefaultPlaceholder = Default(
        generate_unique_id
    ),
    strict_content_type: bool | DefaultPlaceholder = Default(True),
) -> None:
    route.path = path
    route.endpoint = endpoint
    route.stream_item_type = None
    if isinstance(response_model, DefaultPlaceholder):
        return_annotation = get_typed_return_annotation(endpoint)
        if lenient_issubclass(return_annotation, Response):
            response_model = None
        else:
            stream_item = get_stream_item_type(return_annotation)
            if stream_item is not None:
                # Extract item type for JSONL or SSE streaming when
                # response_class is DefaultPlaceholder (JSONL) or
                # EventSourceResponse (SSE).
                # ServerSentEvent is excluded: it's a transport
                # wrapper, not a data model, so it shouldn't feed
                # into validation or OpenAPI schema generation.
                if (
                    isinstance(response_class, DefaultPlaceholder)
                    or lenient_issubclass(response_class, EventSourceResponse)
                ) and not lenient_issubclass(stream_item, ServerSentEvent):
                    route.stream_item_type = stream_item
                response_model = None
            else:
                response_model = return_annotation
    route.response_model = response_model
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
    if route.response_model:
        assert is_body_allowed_for_status_code(status_code), (
            f"Status code {status_code} must not have a response body"
        )

    def _response_field(self):
        if self.response_model:
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

    def _response_fields(self) -> dict[Union[int, str], ModelField]:
        response_fields: dict[Union[int, str], ModelField] = {}
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

    def _get_flat_dependant(self) -> Dependant:
        return get_flat_dependant(self.dependant)

    _add_cache_attribute(route, "_flat_dependant", _get_flat_dependant)

    def _embed_body_fields(self):
        return _should_embed_body_fields(self._flat_dependant.body_params)

    _add_cache_attribute(route, "_embed_body_fields", _embed_body_fields)

    def _body_field(self):
        return get_body_field(
            flat_dependant=self._flat_dependant,
            name=self.unique_id,
            embed_body_fields=self._embed_body_fields,
        )

    _add_cache_attribute(route, "body_field", _body_field)

    # Detect generator endpoints that should stream as JSONL or SSE
    def _is_generator(self) -> bool:
        return self.dependant.is_async_gen_callable or self.dependant.is_gen_callable

    _add_cache_attribute(route, "is_generator", _is_generator)

    def _is_sse_stream(self) -> bool:
        return self.is_generator and lenient_issubclass(
            self.response_class, EventSourceResponse
        )

    _add_cache_attribute(route, "is_sse_stream", _is_sse_stream)

    def _is_json_stream(self) -> bool:
        return self.is_generator and isinstance(self.response_class, DefaultPlaceholder)

    _add_cache_attribute(route, "is_json_stream", _is_json_stream)


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
