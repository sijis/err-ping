from errbot import BotPlugin, botcmd


class Ping(BotPlugin):

    @botcmd
    def ping(self, msg, args):
        """ this command responds 'pong' """
        self.send(msg.frm,
                  'pong',
                  message_type=msg.type)
