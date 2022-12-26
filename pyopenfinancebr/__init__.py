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

from . import tools 

__version__ = '0.0.1'

class OpenFinanceBR(object):
    
    def __init__(self, code_bank, client_id, client_secret):
        self.code_bank = code_bank
        self.client_id = client_id
        self.client_secret = client_secret
 
    def __str__(self):
        if not bool(tools.BANKS.get(self.code_bank,False)):
            return f"The OpenFinance for bank ({self.code_bank}) does not exist or is not available"
        else:
            bank = tools.BANKS[self.code_bank]
            if not bank['ACTIVE']:
                return f"The OpenFinance for bank {bank['NAME']} is not available"
            else:
                return f"The OpenFinance for bank {bank['NAME']} is available"
