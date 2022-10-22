import http_pyparser
from typing import List

from .route import Route
from .status import status
from .server import Client


class ProcessRequest:
    def __init__(self, routes: List[Route]) -> None:
        self._routes = routes
