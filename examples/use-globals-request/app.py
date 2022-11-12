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
    process_result = _request.process(client, use_globals=use_globals)

    if process_result:
        response, request_data = process_result
        log.log_request(response, request_data)

        http = http_pyparser.response.make_response(response)
        client.send_message(http)
        client.destroy()


server = Server()
server.start('127.0.0.1', 2808)
print('Server running in http://127.0.0.1:2808')

while True:
    client = server.wait_client()
    # passing "True" to use_globals
    threading.Thread(target=process, args=(client, True)).start()
