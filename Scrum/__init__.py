#
# Copyright 2011, Adin Scannell
#

"""
List the users in a channel in a random order.
"""

import supybot
import supybot.world as world

__version__  = "git"
__author__   = supybot.Author("Adin Scannell", "amscanne", "adin@scannell.ca")
__url__      = 'http://github.com/amscanne/supybot-scrum'

import config
import plugin
reload(plugin)
