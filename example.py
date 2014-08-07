from pyfpds import Contracts

c = Contracts()
records = c.get(piid='N0001976C0009', vendor_duns="000000000")
print(records)
