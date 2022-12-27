from pyopenfinancebr import OpenFinanceBR

itau = OpenFinanceBR('SANDBOX','341','client_id','client_secret')

print(itau)

print(itau.URL())
