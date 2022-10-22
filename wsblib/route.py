from typing import Callable


class Route:
    def __init__(self, callback: Callable, path: str, methods: list = ['GET']) -> None:
        self._path = path
        self._methods = methods
        self._callback = callback
