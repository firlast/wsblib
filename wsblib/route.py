"""
Contains a `Route` class that stores and manipulates information
of a created route, such as path, accepted methods and the callback function.
"""

from types import FunctionType
from http_pyparser import response, parser

from .exceptions import InvalidRouteResponseError


class Route:
    def __init__(self, callback: FunctionType, path: str, methods: tuple = ('GET',)) -> None:
        self._path = path
        self._methods = methods
        self._callback = callback

    def _register_dynamic_route(self) -> None:
        split_path = self._path.split('/')        
        split_path.remove('')

        parameters = []
        no_parameters = []

        for index, i in enumerate(split_path):
            if i.startswith('<') and i.endswith('>'):
                i = i.replace('<', '')
                i = i.replace('>', '')
                i = i.replace(' ', '')

                parameter = i.split(':')

                if len(parameter) == 2:
                    var_type, name = parameter
                else:
                    var_type = 'any'
                    name = i

                parameters.append({'index': index, 'var_type': var_type, 'name': name})
            else:
                no_parameters.append({'index': index, 'name': i})

        # register registering dynamic route variables
        self._parameters = parameters
        self._no_parameters = no_parameters

    def match_route(self, path: str) -> bool:
        """Checks if the path specified by the "path"
        argument is the same as the path of the registered route.

        :param path: Path to check
        :type path: str
        :return: Comparison result
        :rtype: bool
        """

        return self._path == path

    def accept_method(self, method: str) -> bool:
        """Checks if the method passed by the
        argument is accepted by the route.

        :param method: HTTP method
        :type method: str
        :return: Check result
        :rtype: bool
        """

        return method in self._methods

    def get_route_response(self, request: parser.HTTPData) -> response.Response:
        """Gets the return of the route's callback
        function to use as the route's response.

        The `request` argument is only passed as
        an argument to the callback function, if it
        requests, so that it can get data from the request.

        :param request: Request data
        :type request: parser.HTTPData
        :raises InvalidRouteResponseError: If the route returns None,
        or a boolean value.
        :return: Route response in Response object;
        :rtype: response.Response
        """

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
