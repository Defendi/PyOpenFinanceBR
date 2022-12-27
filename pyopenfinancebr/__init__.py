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

BANKS = {
    '001': {'NAME': 'BANCO DO BRASIL S.A.', 'ACTIVE': False, 'URL': False},
    '033': {'NAME': 'BANCO SANTANDER (BRASIL) S.A.', 'ACTIVE': False, 'URL': False},
    '104': {'NAME': 'CAIXA ECONOMICA FEDERAL', 'ACTIVE': False, 'URL': False},
    '341': {'NAME': 'ITAÚ UNIBANCO S.A.', 'ACTIVE': True, 'URL': url.Itau},
}

class OpenFinanceBR(object):
    
    _url_class = False
    _mode = False
    _code_bank = False
    
    def __init__(self, mode, code_bank, client_id, client_secret):
        self._set_mode(mode)
        self._set_code_bank(code_bank)
        self._client_id = client_id
        self._client_secret = client_secret
        self.session = requests.Session()
 
    def __str__(self):
        if not bool(BANKS.get(self._code_bank,False)):
            return f"The OpenFinance for bank ({self.code_bank}) does not exist or is not available"
        else:
            bank = BANKS[self._code_bank]
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
        self._set_code_bank(value)

    def _set_code_bank(self, code_bank):
        if code_bank in BANKS:
            self._code_bank = code_bank
        else:
            raise Exception("Sorry, select the valid code bank")  
        self._set_url()
       
    @property
    def Mode(self):
        return self._mode
    
    @Mode.setter
    def Mode(self, value):
        self._mode = self._set_mode(value)
    
    def _set_mode(self, mode):
        if bool(mode) and mode in tools.VALID_MODE:
            self._mode = mode
        else:
            raise Exception("Sorry, select the valid mode for use")  
        self._set_url()
            
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

    def URL(self):
        if bool(self._url_class):
            return str(self._url_class)
        return 'URL not defined'

    def _set_url(self):
        if BANKS.get(self._code_bank, False) and BANKS[self._code_bank]['ACTIVE']:
            self._url_class = BANKS[self._code_bank]['URL'](mode=self._mode)
        else:
            self._url_class = False
     
    def _validate_request(self):
        errors = []
        if not bool(self._url_class):
            errors.append("Select the mode or/and bank code for url generation")
        if not bool(self._client_secret):
            errors.append("Set the client secret")
        if not bool(self._client_id):
            errors.append("Set the client ID")
        return errors
    

        
        