# simple framework using WSBLib

from wsblib.route import Route
from wsblib.server import Client, Server
from wsblib.request import ProcessRequest

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
