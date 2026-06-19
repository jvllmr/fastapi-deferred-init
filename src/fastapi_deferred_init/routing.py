from enum import Enum
from functools import cached_property
from typing import (
    Any,
    Callable,
    Optional,
    Union,
)
from collections.abc import Sequence

from starlette.routing import BaseRoute, compile_path

from starlette.types import ASGIApp, Lifespan

from fastapi import params, routing  # type: ignore[attr-defined]
from fastapi.datastructures import Default, DefaultPlaceholder
from fastapi.responses import JSONResponse, Response
from fastapi.types import IncEx
from fastapi.utils import (
    generate_unique_id,
)


import typing as t


def _getattr(route, name) -> t.Any:
    return object.__getattribute__(route, name)


class DeferringAPIRoute(routing.APIRoute):
    def __prepopulate_route(self, route: routing._APIRouteLike, **kw: t.Any) -> None:
        for k, v in kw.items():
            setattr(route, k, v)
            self.__prepopulated_fields.add(k)

    def __getattribute__(self, name: str) -> t.Any:
        if (
            not name.startswith("_DeferringAPIRoute__")
            and not name.startswith("__")
            and not self.__populated
            and name not in self.__prepopulated_fields
        ):
            raise ValueError("reee!")
            print("populating...")
            self.__populated = True
            routing._populate_api_route_state(
                t.cast(routing._APIRouteLike, self),
                object.__getattribute__(self, "path"),
                self.endpoint,
                response_model=self.response_model,
                status_code=self.status_code,
                tags=self.tags,
                dependencies=self.dependencies,
                summary=self.summary,
                description=self.description,
                response_description=self.response_description,
                responses=self.responses,
                deprecated=self.deprecated,
                name=self.name,
                methods=self.methods,
                operation_id=self.operation_id,
                response_model_include=self.response_model_include,
                response_model_exclude=self.response_model_exclude,
                response_model_by_alias=self.response_model_by_alias,
                response_model_exclude_unset=self.response_model_exclude_unset,
                response_model_exclude_defaults=self.response_model_exclude_defaults,
                response_model_exclude_none=self.response_model_exclude_none,
                include_in_schema=self.include_in_schema,
                response_class=self.response_class,
                dependency_overrides_provider=self.dependency_overrides_provider,
                callbacks=self.callbacks,
                openapi_extra=self.openapi_extra,
                generate_unique_id_function=self.generate_unique_id_function,
                strict_content_type=self.strict_content_type,
            )
            print("populated!")
        return object.__getattribute__(self, name)

    def __init__(
        self,
        path: str,
        endpoint: t.Callable[..., t.Any],
        *,
        response_model: t.Any = Default(None),
        status_code: int | None = None,
        tags: list[str | Enum] | None = None,
        dependencies: t.Sequence[params.Depends] | None = None,
        summary: str | None = None,
        description: str | None = None,
        response_description: str = "Successful Response",
        responses: dict[int | str, dict[str, t.Any]] | None = None,
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
        dependency_overrides_provider: t.Any | None = None,
        callbacks: list[BaseRoute] | None = None,
        openapi_extra: dict[str, t.Any] | None = None,
        generate_unique_id_function: t.Callable[["routing.APIRoute"], str]
        | DefaultPlaceholder = Default(generate_unique_id),
        strict_content_type: bool | DefaultPlaceholder = Default(True),
    ) -> None:
        self.__populated = False
        self.__prepopulated_fields: set[str] = {"app", "path_regex"}
        for k in self.__dir__():
            self.__prepopulated_fields.add(k)
        self.__prepopulate_route(
            t.cast(routing._APIRouteLike, self),
            path=path,
            endpoint=endpoint,
            response_model=response_model,
            status_code=status_code,
            tags=tags,
            dependencies=dependencies,
            summary=summary,
            description=description,
            response_description=response_description,
            responses=responses,
            deprecated=deprecated,
            name=name,
            methods=methods,
            operation_id=operation_id,
            response_model_include=response_model_include,
            response_model_exclude=response_model_exclude,
            response_model_by_alias=response_model_by_alias,
            response_model_exclude_unset=response_model_exclude_unset,
            response_model_exclude_defaults=response_model_exclude_defaults,
            response_model_exclude_none=response_model_exclude_none,
            include_in_schema=include_in_schema,
            response_class=response_class,
            dependency_overrides_provider=dependency_overrides_provider,
            callbacks=callbacks,
            openapi_extra=openapi_extra,
            generate_unique_id_function=generate_unique_id_function,
            strict_content_type=strict_content_type,
        )
        self.path_regex, self.path_format, self.param_convertors = compile_path(path)

    @cached_property
    def app(self):
        return routing.request_response(self.get_route_handler())


class DeferringAPIRouter(routing.APIRouter):
    def __init__(
        self,
        *,
        prefix: str = "",
        tags: Optional[list[Union[str, Enum]]] = None,
        dependencies: Optional[Sequence[params.Depends]] = None,
        default_response_class: type[Response] = Default(JSONResponse),
        responses: Optional[dict[Union[int, str], dict[str, Any]]] = None,
        callbacks: Optional[list[BaseRoute]] = None,
        routes: Optional[list[BaseRoute]] = None,
        redirect_slashes: bool = True,
        default: Optional[ASGIApp] = None,
        dependency_overrides_provider: Optional[Any] = None,
        route_class: type[routing.APIRoute] = DeferringAPIRoute,
        on_startup: Optional[Sequence[Callable[[], Any]]] = None,
        on_shutdown: Optional[Sequence[Callable[[], Any]]] = None,
        lifespan: Optional[Lifespan[Any]] = None,
        deprecated: Optional[bool] = None,
        include_in_schema: bool = True,
        generate_unique_id_function: Callable[[routing.APIRoute], str] = Default(
            generate_unique_id
        ),
        strict_content_type: bool = Default(True),
    ) -> None:
        super().__init__(
            prefix=prefix,
            tags=tags,
            dependencies=dependencies,
            default_response_class=default_response_class,
            responses=responses,
            callbacks=callbacks,
            routes=routes,
            redirect_slashes=redirect_slashes,
            default=default,
            dependency_overrides_provider=dependency_overrides_provider,
            route_class=route_class,
            on_startup=on_startup,
            on_shutdown=on_shutdown,
            lifespan=lifespan,
            deprecated=deprecated,
            include_in_schema=include_in_schema,
            generate_unique_id_function=generate_unique_id_function,
            strict_content_type=strict_content_type,
        )
