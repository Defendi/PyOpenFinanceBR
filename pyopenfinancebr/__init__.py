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

import requests
import logging

from . import tools
from . import url

logger = logging.getLogger(__name__)

__version__ = '0.0.1'

class OpenFinanceBR(object):
    
    valid_to = False
    
    def __init__(self, code_bank, client_id, client_secret):
        self._code_bank = code_bank
        self._client_id = client_id
        self._client_secret = client_secret
        self.session = requests.Session()
 
    def __str__(self):
        if not bool(tools.BANKS.get(self._code_bank,False)):
            return f"The OpenFinance for bank ({self.code_bank}) does not exist or is not available"
        else:
            bank = tools.BANKS[self._code_bank]
            if not bank['ACTIVE']:
                return f"The OpenFinance for bank {bank['NAME']} is not available"
            elif bool(self._client_id) and bool(self._client_secret):
                return f"The OpenFinance for bank {bank['NAME']} is available, with the credentials: client Id = {self._client_id} and client secret = {self._client_secret}"
            else:
                return f"The OpenFinance for bank {bank['NAME']} is available, enter your credentials to be able to connect"

    @property
    def CodeBank(self):
        return self._code_bank
    
    @CodeBank.setter
    def CodeBank(self, value):
        if value in tools.BANKS:
            self._code_bank = value
            
    @property
    def ClientId(self):
        return self._client_id
    
    @ClientId.setter
    def ClientId(self, value):
        self._client_id = value
            
    @property
    def ClientSecret(self):
        return self._client_secret
    
    @ClientSecret.setter
    def ClientSecret(self, value):
        self._client_secret = value
