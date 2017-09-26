# 32.py

import pickle


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.message = "Nothing happens"

    # Returns the current object state to be serialized by pickle
    def __getstate__(self):
        # Here we create a copy of the current dictionary, to modify the copy,
        # not the original object
        new = self.__dict__.copy()
        new.update({"message": "I'm being serialized!!"})
        return new

m = Person("Bob", 30)
print(m.message)
serial = pickle.dumps(m)
m2 = pickle.loads(serial)
print(m2.message)
print(m.message)  # The original object is "the same"
