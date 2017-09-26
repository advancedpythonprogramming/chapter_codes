# 30.py

import pickle

list_ = [1, 2, 3, 7, 8, 3]
with open("my_list", 'wb') as file:
    pickle.dump(list_, file)

with open("my_list", 'rb') as file:
    my_list = pickle.load(file)
    # This will generate an error if the object is not same we saved
    assert my_list == list_
