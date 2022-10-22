import sys
import socket

import bupytest

sys.path.insert(0, './')

from wsblib import server


class TestSocket(bupytest.UnitTest):
    def __init__(self):
        super().__init__()

        self.server = server.Server()
        self.server.start('localhost', 2808)

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


if __name__ == '__main__':
    bupytest.this()
