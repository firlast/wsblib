from types import FunctionType

from .exceptions import InvalidResponseError
from .request import RequestData

from http_pyparser import response


class Error:
    def __init__(self, callback: FunctionType, status_code: int) -> None:
        self._callback = callback
        self._status_code = status_code

    def match_status_code(self, status_code: int) -> bool:
        return self._status_code == status_code
