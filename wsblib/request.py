import http_pyparser
from typing import List

from .route import Route
from .status import status
from .server import Client


class ProcessRequest:
    def __init__(self, routes: List[Route]) -> None:
        self._routes = routes

    def process_request(self, client: Client) -> None:
        # get client request
        message = client.get_message()

        if not message:
            client.destroy()
        else:
            http_parser = http_pyparser.parser.HTTPParser()
            request = http_parser.parser(message)

            # checking routes
            for route in self._routes:
                if route.match_route(request.path):
                    if route.accept_method(request.method):
                        response = route.get_route_response(request)
                        http_response = http_pyparser.response.make_response(response)

                        client.send_message(http_response)
                        client.destroy()
                    else:
                        response = http_pyparser.response.Response(
                            body='Method Not Allowed',
                            status=status.method_not_allowed_405
                        )

                        http_response = http_pyparser.response.make_response(response)
                        client.send_message(http_response)
                        client.destroy()
