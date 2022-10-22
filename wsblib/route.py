from types import FunctionType
from http_pyparser import response, parser

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

    def get_route_response(self, request: parser.HTTPData) -> response.Response:
        try:
            callback_response = self._callback.__call__(request)
        except TypeError:
            callback_response = self._callback.__call__()

        if not callback_response:
            raise InvalidRouteResponseError(f'Route "{self._path}" returned a invalid response')
        else:
            if isinstance(callback_response, tuple):
                # getting body and status of response
                # in use cases of: return "Hello", 200.
                body, status = callback_response
                final_response = response.Response(body, status=status)
            elif isinstance(callback_response, response.Response):
                final_response = callback_response
            else:
                final_response = response.Response(callback_response)

            return final_response
