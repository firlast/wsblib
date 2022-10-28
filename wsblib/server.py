import socket
from typing import Tuple, Union


class Client:
    def __init__(self, client: socket.socket, address: tuple) -> None:
        self._client = client
        self._address = address

    def send_message(self, message: str) -> None:
        self._client.send(message.encode())

    def get_address(self) -> tuple:
        """Get client address in a tuple (host and port).

        :return: Client address.
        :rtype: tuple
        """

        return self._address

    def get_message(self) -> Union[None, str]:
        """Get the message sent by the client socket.

        :return: Client message.
        :rtype: Union[None, str]
        """

        try:
            self._client.settimeout(1)
            message = self._client.recv(1024)
        except socket.timeout:
            return None

        self._client.settimeout(None)
        return message.decode()

    def destroy(self) -> None:
        self._client.shutdown(socket.SHUT_RDWR)
        self._client.close()


class Server(object):
    def __init__(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def start(self, host: str, port: int) -> None:
        address = (host, port)

        self._socket.bind(address)
        self._socket.listen(128)

    def wait_client(self) -> Client:
        csocket, address = self._socket.accept()
        client = Client(csocket, address)

        return client
