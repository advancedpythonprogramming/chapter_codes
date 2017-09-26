# 33.py

import pickle


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.message = "Nothing happens"

    # Returns the current object state to be serialized by pickle
    def __getstate__(self):
        # Here we create a copy of the current dictionary, to modify the copy,
        #  not the original object
        new = self.__dict__.copy()
        new.update({"message": "I'm being serialized!!"})
        return new

    def __setstate__(self, state):
        print("deserialized object, setting its state...\n")
        state.update({"name": state["name"] + " deserialized"})
        self.__dict__ = state

m = Person("Bob", 30)
print(m.name)
serial = pickle.dumps(m)
m2 = pickle.loads(serial)
print(m2.name)
