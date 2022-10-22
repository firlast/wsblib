import socket


class Server(object):
    def __init__(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def start(self, host: str, port: int) -> None:
        address = (host, port)

        self._socket.bind(address)
        self._socket.listen(128)
