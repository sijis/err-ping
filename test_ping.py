import ping
from errbot.backends.test import testbot, push_message, pop_message
from errbot import plugin_manager


class TestPing(object):
    extra_plugin_dir = '.'

    def test_ping(self, testbot):
        push_message('!ping')
        assert 'pong' in pop_message()
