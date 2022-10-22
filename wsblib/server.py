import socket
from typing import Tuple, Union


class Client:
    def __init__(self, client: socket.socket, address: socket._RetAddress) -> None:
        self._client = client
        self._address = address

    def get_address(self) -> socket._RetAddress:
        """Get client address in a tuple (host and port).

        :return: Client address.
        :rtype: socket._RetAddress
        """

        return self._address

    def get_message(self) -> Union[None, str]:
        """Get the message sent by the client socket.

        :return: Client message.
        :rtype: Union[None, str]
        """

        try:
            self._client.settimeout(1.5)
            message = self._client.recv(2048)
        except socket.timeout:
            return None

        self._client.settimeout(None)
        return message.decode()

    def destroy(self) -> None:
        self._client.shutdown()
        self._client.close()


class Server(object):
    def __init__(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def start(self, host: str, port: int) -> None:
        address = (host, port)

        self._socket.bind(address)
        self._socket.listen(128)

    def wait_client(self) -> Tuple[socket.socket, socket._RetAddress]:
        client = self._socket.accept()
        return client