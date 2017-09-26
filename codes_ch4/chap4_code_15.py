class MyMetaClass(type):

    def __new__(meta, clsname, bases, clsdict):
        print('-----------------------------------')
        print("Creating Class: {} ".format(clsname))
        print(meta)
        print(bases)
        # Suppose we want to have a mandatory attribute
        clsdict.update(dict({'mandatory_attribute': 10}))
        print(clsdict)
        return super().__new__(meta, clsname, bases, clsdict)
        # we are calling 'type' __new__ method after doing the desired
        # modifications. Note hat this method is the one that would have
        # been called had we not used this personalized metaclass


class MyClass(metaclass=MyMetaClass):

    def func(self, params):
        pass

    my_param = 4

m1 = MyClass()
print(m1.mandatory_attribute)
