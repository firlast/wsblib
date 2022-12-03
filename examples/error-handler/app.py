# using error handler

from wsblib.route import Route
from wsblib.server import Client, Server
from wsblib.request import ProcessRequest
from wsblib.errors import Error
from wsblib import log

import http_pyparser

import threading


def index():
    return 'Hello World!'

# callback function to 404 error
def not_found_error():
    return 'Sorry, this page is not found!'


index_route = Route(index, '/')
routes = (index_route,)

# creating Error instance to 404 error
error_not_found = Error(not_found_error, 404)
request = ProcessRequest(routes, [error_not_found])


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
