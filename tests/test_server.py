import sys

import bupytest
from http_pyparser.response import Response
from http_pyparser.parser import HTTPData

sys.path.insert(0, './')

from wsblib import route


class TestServer(bupytest.UnitTest):
    def __init__(self):
        super().__init__()

        def callback():
            return 'Hello World!'

        def callback_2():
            return {'status': 'created', 'id': 28}, 201

        self.index_route = route.Route(callback, '/', methods=('GET', 'POST'))
        self.about_route = route.Route(callback_2, '/about')

    def test_route(self):
        self.assert_true(self.index_route.match_route('/'))
        self.assert_false(self.index_route.match_route('/index'))
        self.assert_true(self.index_route.accept_method('POST'))
        self.assert_true(self.index_route.accept_method('GET'))
        self.assert_false(self.index_route.accept_method('PUT'))

        self.assert_true(self.about_route.match_route('/about'))
        self.assert_false(self.about_route.match_route('/sobre'))
        self.assert_true(self.about_route.accept_method('GET'))
        self.assert_false(self.about_route.accept_method('POST'))

        fake_http_data = HTTPData()

        # get /index route response
        index_response = self.index_route.get_route_response(fake_http_data)

        self.assert_true(isinstance(index_response, Response))
        self.assert_expected(index_response.body, 'Hello World!')
        self.assert_expected(index_response.content_type, 'text/html')
        self.assert_expected(index_response.status, 200)

        # get /about route response
        about_response = self.about_route.get_route_response(fake_http_data)

        self.assert_true(isinstance(about_response, Response))
        self.assert_expected(about_response.body, {'status': 'created', 'id': 28})
        self.assert_expected(about_response.content_type, 'text/html')
        self.assert_expected(about_response.status, 201)


if __name__ == '__main__':
    bupytest.this()
