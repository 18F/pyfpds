from pyfpds import Contracts

c = Contracts()

#filter by a specific contract ID number
records = c.get(piid="FA865014M5002")

r = records[0]['content']['award']

#pretty print the first record
c.pretty_print(r)

print("Length: {0}".format(len(records)))
