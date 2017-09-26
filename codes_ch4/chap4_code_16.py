class MyMetaClass(type):

    def __call__(cls, *args, **kwargs):
        print("__call__ of  {}".format(str(cls)))
        print("__call__ *args= {}".format(str(args)))
        return super().__call__(*args, **kwargs)


class MyClass(metaclass=MyMetaClass):

    def __init__(self, a, b):
        print("MyClass object with a=%s, b=%s" % (a, b))

print('creating a new object...')
obj1 = MyClass(1, 2)
