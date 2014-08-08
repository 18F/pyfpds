from pyfpds import Contracts, pretty_print

c = Contracts()
#records = c.get(piid='INA14PD00431')
records = c.get(vendor_name="lockheed")
pretty_print(records)
print("Length: {0}".format(len(records)))
print(c.query_url)
#print(records)
