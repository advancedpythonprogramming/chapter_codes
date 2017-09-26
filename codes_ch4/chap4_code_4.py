name = "MyClass"
my_class = """
class %s():
    def __init__(self, a):
        self.at = a
""" % (name)
exec(my_class)
e = MyClass(8)
print(e.at)
