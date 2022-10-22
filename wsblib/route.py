from typing import Any
from types import FunctionType

from .exceptions import InvalidRouteResponseError


class Route:
    def __init__(self, callback: FunctionType, path: str, methods: tuple = ('GET',)) -> None:
        self._path = path
        self._methods = methods
        self._callback = callback

    def match_route(self, path: str) -> bool:
        return self._path == path

    def accept_method(self, method: str) -> bool:
        return method in self._methods

    def get_route_response(self, request: Any) -> Any:
        try:
            response = self._callback.__call__(request)
        except TypeError:
            response = self._callback.__call__()

        if not response:
            raise InvalidRouteResponseError(f'Route "{self._path}" returned a invalid response')
        else:
            return response
