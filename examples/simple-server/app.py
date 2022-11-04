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
