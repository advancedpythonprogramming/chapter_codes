# 7.py

# AttributeError exception: incorrect use of methods of a class or data type.
# In this example the class Car has only defined the method move, but the
# program tries execute the method stop() that doesn't exist


class Car:
    def __init__(self, doors=4):
        self.doors = doors

    def mover(self):
        print('avanzando')

chevi = Car()
chevi.stop()
