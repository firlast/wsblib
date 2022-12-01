# simple server with threads using WSBLib

from wsblib.route import Route
from wsblib.server import Client, Server
from wsblib.request import ProcessRequest
from wsblib.request import RequestData as request
from wsblib import log

import http_pyparser

import threading


def index():
    return 'Hello World!'


def about():
    return 'About route'


# see that it is not necessary to add the "request" argument in the route function
def echo():
    message = request.parameters.get('message')
    return 'You say: ' + message


index_route = Route(index, '/')
about_route = Route(about, '/about')
echo_route = Route(echo, '/echo/<message>')
routes = (index_route, about_route, echo_route)

_request = ProcessRequest(routes)


def process(client: Client, use_globals: bool):
    # passing "True" to use_globals
    processed_request = _request.process(client)

    if processed_request:
        request_data = processed_request.request
        process_type = processed_request.type

        if process_type == 'route':
            response = processed_request.route.get_route_response(request_data, use_globals)
        else:
            response = processed_request.route.get_callback_response(request_data)

        http = http_pyparser.response.make_response(response)

        log.log_request(response, request_data)
        client.send_message(http)
        client.destroy()


server = Server()
server.start('127.0.0.1', 2808)
print('Server running in http://127.0.0.1:2808')

while True:
    client = server.wait_client()
    threading.Thread(target=process, args=(client, True)).start()
