#*************************************************************************#
# 🄯  2023 Alexandre Defendi, OpusSystem                                    #
#                                                                         #
#      ____                   _____            __                         #
#     / __ \____  __  _______/ ___/__  _______/ /____  ____ ___           #
#    / / / / __ \/ / / / ___/\__ \/ / / / ___/ __/ _ \/ __ `__ \          #
#   / /_/ / /_/ / /_/ (__  )___/ / /_/ (__  ) /_/  __/ / / / / /          #
#   \____/ .___/\__,_/____//____/\__, /____/\__/\___/_/ /_/ /_/           #
#       /_/                     /____/                                    #
#                                                                         #
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).      #
#*************************************************************************#

from .tools import SANDBOX, PRODUCTION, BANKS, VALID_MODE

class urlBank(object):
    _mode = False
    
    def __init__(self, mode=False):
        if bool(mode) and mode in VALID_MODE:
            self._mode = mode
    
    @property
    def mode(self):
        return self._mode
    
    @mode.setter
    def mode(self, value):
        if bool(value) and value in VALID_MODE:
            self._mode = value
        else:
            raise Exception("Sorry, this mode does not exist") 

    @property
    def url(self):
        return False

class urlItau(urlBank):
    @property
    def url(self):
        if self._mode == SANDBOX:
            return 'https://api.itau/open-banking'
        elif self._mode == PRODUCTION:
            return False
        else:
            raise Exception("Sorry, select the mode for use")  
        return False
