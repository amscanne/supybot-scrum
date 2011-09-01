#
# Copyright 2011, Adin Scannell
#

from supybot import callbacks
from supybot.commands import wrap

import random

class Scrum(callbacks.Plugin):
    """ Simple plugin to support scrums in IRC channels. """

    threaded = True

    def __init__(self, irc):
        self.__parent = super(Scrum, self)
        self.__parent.__init__(irc)

    def who(self, irc, msg, args, name, url, username, password):
        """who

        Sort the members of the channel and spit out an order for
        the current scrum.
        """
        for channel in irc.state.channels:
            users = irc.state.channels[channel].users
            random.shuffle(users)
            irc.queueMsg(ircmsgs.privmsg(channel, ','.join(users)))
        irc.noReply()

    who = wrap(who)

Class = Scrum
