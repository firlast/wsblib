import sys

import bupytest
from http_pyparser.response import Response
from http_pyparser.parser import HTTPData

from mock import SocketMock

sys.path.insert(0, './')

from wsblib import route
from wsblib import server
from wsblib import request as wsb_request


class TestServer(bupytest.UnitTest):
    def __init__(self):
        super().__init__()

        def callback():
            return 'Hello World!'

        def callback_2(request):
            id = request.query.get('id')
            return {'name': 'WSBLib', 'id': int(id)}, 201

        self.index_route = route.Route(callback, '/', methods=('GET', 'POST'))
        self.project_route = route.Route(callback_2, '/project')

    def test_route(self):
        self.assert_true(self.index_route.match_route('/'))
        self.assert_false(self.index_route.match_route('/index'))
        self.assert_true(self.index_route.accept_method('POST'))
        self.assert_true(self.index_route.accept_method('GET'))
        self.assert_false(self.index_route.accept_method('PUT'))

        fake_http_data = HTTPData()
        index_response = self.index_route.get_route_response(fake_http_data)

        self.assert_true(isinstance(index_response, Response))
        self.assert_expected(index_response.body, 'Hello World!')
        self.assert_expected(index_response.content_type, 'text/html')
        self.assert_expected(index_response.status, 200)

    def test_process_request(self):
        project_route_http = ('GET /project?id=28 HTTP/1.1\r\n'
                              'Cookie: projectId=28\r\n\r\n')

        route_list = [self.index_route, self.project_route]
        process = wsb_request.ProcessRequest(route_list)

        mock_socket = SocketMock(project_route_http)
        client = server.Client(mock_socket, ('127.0.0.1', 5500))

        request_processed = process.process(client)

        # check request data
        self.assert_expected(request_processed.request.cookies, {'projectId': '28'})
        self.assert_expected(request_processed.request.path, '/project')
        self.assert_expected(request_processed.request.query, {'id': '28'})

        # changing query data from request data
        request_processed.request.query = {'id': '30'}
        self.assert_expected(request_processed.request.query, {'id': '30'})

        # get route response
        response = request_processed.get_response()

        # check response data
        self.assert_expected(response.body, {'name': 'WSBLib', 'id': 30})
        self.assert_expected(response.content_type, 'text/html')
        self.assert_expected(response.status, 201)


if __name__ == '__main__':
    bupytest.this()
