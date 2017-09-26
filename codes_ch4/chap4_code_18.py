class MyMetaClass(type):

    def __init__(cls, name, bases, dic):
        print("__init__ of  {}".format(str(cls)))
        super().__init__(name, bases, dic)


class MyClass(metaclass=MyMetaClass):

    def __init__(self, a, b):
        print("MyClass object with a=%s, b=%s" % (a, b))

print('creating a new object...')
obj1 = MyClass(1, 2)
