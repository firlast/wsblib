from types import FunctionType


class Error:
    def __init__(self, callback: FunctionType, status_code: int) -> None:
        self._callback = callback
        self._status_code = status_code
