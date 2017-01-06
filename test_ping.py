import ping

pytest_plugins = ["errbot.backends.test"]
extra_plugin_dir = '.'


class TestPing(object):
    extra_plugin_dir = '.'

    def test_ping(self, testbot):
        testbot.push_message('!ping')
        assert 'pong' in testbot.pop_message()
