import sys

from twisted.internet import reactor, task, defer, protocol
from twisted.python import log
from twisted.words.protocols import irc
from twisted.web.client import getPage
from twisted.application import internet, service

from plugins.teratome import teratome

HOST = 'irc.freenode.net'
PORT = 6667
CHANNELS = ['#terabottest']
NICK = 'terabot'

class TeraBotProtocol(irc.IRCClient):
    nickname = NICK 

    def signedOn(self):
        # Called when signed in
        for channel in self.factory.channels:
            self.join(channel)

    def joined(self, channel):
        """This will get called when the bot joins the channel."""
        self.msg(channel, 'Hello!')

    # Called when a PRIVMSG is received.
    def privmsg(self, user, channel, msg):
        """This will get called when the bot receives a message."""
        user = user.split('!', 1)[0]
        
        # Check to see if they're sending me a private message
        if channel == self.nickname:
            msg = "It isn't nice to whisper!  Play nice with the group."
            self.msg(user, msg)
            return

        # Otherwise check to see if it is a message directed at me
        if msg.startswith(self.nickname + ":"):
            msg = "%s: I am just a bot" % user
            self.msg(channel, msg)

        if msg.startswith('!'):
            message = "Querying data..."
            print msg
            query = teratome(msg[1:]) 

            self.msg(channel, message)

            # Running teratome() to make query
            for i in query:
                self.msg(channel, str(i))


    def action(self, user, channel, msg):
        """This will get called when the bot sees someone do an action."""
        user = user.split('!', 1)[0]

class TeraBotFactory(protocol.ReconnectingClientFactory):
    protocol = TeraBotProtocol
    channels = CHANNELS 

if __name__ == '__main__':
    reactor.connectTCP(HOST, PORT, TeraBotFactory())
    log.startLogging(sys.stdout)
    reactor.run() 
