# instance_apartment.py

from create_apartment import Apartment

d1 = Apartment(_id=1, mts2=100, value=5000)

print("sold?", d1.sold)
d1.sell()
print("sold?", d1.sold)
d1.sell()
