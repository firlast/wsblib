# simple server with threads using WSBLib

from wsblib.route import Route
from wsblib.server import Client, Server
from wsblib.request import ProcessRequest
from wsblib.request import RequestData
from wsblib import log

import http_pyparser

import threading


def index():
    return 'Hello World!'


def about():
    return 'About route'


def echo(request: RequestData):
    message = request.parameters.get('message')
    return 'You say: ' + message


index_route = Route(index, '/')
about_route = Route(about, '/about')
echo_route = Route(echo, '/echo/<message>')
routes = (index_route, about_route, echo_route)

request = ProcessRequest(routes)


def process(client: Client):
    processed_request = request.process(client)

    if processed_request:
        request_data = processed_request.request
        response = processed_request.get_response()

        http = http_pyparser.response.make_response(response)

        log.log_request(response, request_data)
        client.send_message(http)
        client.destroy()


server = Server()
server.start('127.0.0.1', 2808)
print('Server running in http://127.0.0.1:2808')

while True:
    client = server.wait_client()
    threading.Thread(target=process, args=(client,)).start()
