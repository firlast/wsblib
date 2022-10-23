import sys

import bupytest

sys.path.insert(0, './')

from wsblib import route


class TestRoute(bupytest.UnitTest):
    def __init__(self):
        super().__init__()

    def test_route(self):
        def callback():
            return 'Hello World!'

        def callback_2():
            return 'Just "hello"'

        index_route = route.Route(callback, '/', methods=('GET', 'POST'))
        about_route = route.Route(callback_2, '/about')

        self.assert_true(index_route.match_route('/'))
        self.assert_false(index_route.match_route('/index'))
        self.assert_true(index_route.accept_method('POST'))
        self.assert_true(index_route.accept_method('GET'))
        self.assert_false(index_route.accept_method('PUT'))

        self.assert_true(about_route.match_route('/about'))
        self.assert_false(about_route.match_route('/sobre'))
        self.assert_true(about_route.accept_method('GET'))
        self.assert_false(about_route.accept_method('POST'))


if __name__ == '__main__':
    bupytest.this()
