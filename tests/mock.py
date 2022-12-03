class SocketMock:
    def __init__(self, message: str):
        self._message = message.encode()

    def send(self, data) -> None:
        pass

    def settimeout(self, data) -> None:
        pass

    def recv(self, bufsize) -> bytes:
        return self._message

    def shutdown(self, data) -> None:
        pass

    def close(self) -> None:
        pass
