def create_class(name):
    if name == 'MyClass':
        class MyClass:  # Usual way of creating a class
            pass
        return MyClass
    else:
        class OtherClass:
            pass
        return OtherClass

c1 = create_class('MyClass')
print(c1())
