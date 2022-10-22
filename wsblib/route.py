from typing import Callable


class Route:
    def __init__(self, callback: Callable, path: str, methods: list = ['GET']) -> None:
        self.path = path
        self.methods = methods
        self.callback = callback
