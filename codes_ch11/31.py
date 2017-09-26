# 31.py

import pickle

my_object = [1, 2, 3, 4]
serial = pickle.dumps(my_object, protocol=2)
