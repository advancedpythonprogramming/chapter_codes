# 39.py

import json
from datetime import datetime


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


class PersonaEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Person):
            return {'Person_id': obj.idn, 'name': obj.name,
                    'age': obj.age, 'marital_status': obj.marital_status,
                    'dob': datetime.now().year - obj.age}
        return super().default(obj)


p1 = Person("Bob", 37, "Single")
p2 = Person("Mark", 33, "Married")
p3 = Person("Peter", 24, "Single")

print("Default serialization:\n")
# With this we serialized using the default method
json_string = json.dumps(p1.__dict__)
print(json_string)

#  Now we serialize with the personalized method
print("\nCustom Serialization:\n")
json_string = json.dumps(p1, cls=PersonaEncoder)
print(json_string)
json_string = json.dumps(p2, cls=PersonaEncoder)
print(json_string)
json_string = json.dumps(p3, cls=PersonaEncoder)
print(json_string)
