class SocketMock:
    def __init__(self, message: str):
        self._message = message.encode()
        self.sent_msg = None

    def send(self, data: bytes) -> None:
        self.sent_msg = data.decode()

    def settimeout(self, data) -> None:
        pass

    def recv(self, bufsize) -> bytes:
        return self._message

    def shutdown(self, data) -> None:
        pass

    def close(self) -> None:
        pass
