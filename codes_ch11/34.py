# 34.py

import json


class Person:

    def __init__(self, name, age, marital_status):
        self.name = name
        self.age = age
        self.marital_status = marital_status
        self.idn = next(Person.gen)

    def get_id():
        cont = 1
        while True:
            yield cont
            cont += 1

    gen = get_id()

p = Person("Bob", 35, "Single")
json_string = json.dumps(p.__dict__)
print("JSON data: ")
print(json_string)
print("Python data: ")
print(json.loads(json_string))
