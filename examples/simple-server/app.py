# simple server with threads using WSBLib

from wsblib.route import Route
from wsblib.server import Client, Server
from wsblib.request import ProcessRequest

import http_pyparser

import threading


def index():
    return 'Hello World!'


def about():
    return 'About route'


index_route = Route(index, '/')
about_route = Route(about, '/about')
routes = (index_route, about_route)

request = ProcessRequest(routes)


def process(client: Client):
    response = request.process(client)

    if response:
        http = http_pyparser.response.make_response(response)
        client.send_message(http)
        client.destroy()


server = Server()
server.start('127.0.0.1', 2808)
print('Server running in http://127.0.0.1:2808')

while True:
    client = server.wait_client()
    threading.Thread(target=process, args=(client,)).start()
