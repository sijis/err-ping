from errbot import BotPlugin, botcmd


class Ping(BotPlugin):

    @botcmd
    def ping(self, msg, args):
        """ this command responds 'pong' """
        return 'pong'
