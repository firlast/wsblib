import http_pyparser
from typing import List, Union

from .route import Route
from .status import status
from .server import Client


class ProcessRequest:
    def __init__(self, routes: List[Route]) -> None:
        self._routes = routes

    def process_request(self, client: Client) -> Union[http_pyparser.Response, bool]:
        # get client request
        message = client.get_message()

        if not message:
            client.destroy()
            response = False
        else:
            http_parser = http_pyparser.parser.HTTPParser()
            request = http_parser.parser(message)

            match_route: Route = None

            # checking routes
            for route in self._routes:
                if route.match_route(request.path):
                    match_route = route
                    break

            # make route response
            if match_route:
                if route.accept_method(request.method):
                    response = route.get_route_response(request)
                else:
                    response = http_pyparser.response.Response(
                        body='Method Not Allowed',
                        status=status.method_not_allowed_405
                    )
            else:
                response = http_pyparser.response.Response(
                    body='Not Found',
                    status=status.not_found_404
                )

        return response
