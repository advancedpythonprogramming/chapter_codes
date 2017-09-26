name = "MyClass"
c2 = type(name, (), {})

# We can do the same with a function
def create_class(name):
    c = type(name, (), {})
    return c

# Here we create the class MyClass2
create_class("MyClass2")()
