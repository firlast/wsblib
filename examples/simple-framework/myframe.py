# simple framework using WSBLib

from wsblib.route import Route
from wsblib.server import Client, Server
from wsblib.request import ProcessRequest
from wsblib import log

import http_pyparser

import threading


class MyFrame:
    def __init__(self) -> None:
        self._routes = []

    def route(self, path: str, methods: list = ['GET']) -> object:
        def decorator(function):
            def wrapper(*args, **kwargs):
                self._routes.append(Route(function, path, methods))
                return function(*args, **kwargs)

            return wrapper()

        return decorator

    def run(self, host: str = '127.0.0.1', port: int = 5500) -> None:
        request = ProcessRequest(self._routes)

        def process(client: Client):
            process = request.process(client)

            if process:
                response, request_data = process
                log.log_request(response, request_data)

                http = http_pyparser.response.make_response(response)
                client.send_message(http)
                client.destroy()


        server = Server()
        server.start(host, port)

        print(f'Server running in http://{host}:{port}')

        while True:
            client = server.wait_client()
            th = threading.Thread(target=process, args=(client,))
            th.start()
