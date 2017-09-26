# 29.py

import pickle

tuple_ = ("a", 1, 3, "hi")
serial = pickle.dumps(tuple_)
print(serial)
print(type(serial))
print(pickle.loads(serial))
