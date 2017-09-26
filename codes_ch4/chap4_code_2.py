class Example:
    pass

x = Example()
print(hasattr(x, 'attr'))
Example.attr = 33
y = Example()
print(y.attr)
Example.attr2 = 54
print(y.attr2)
Example.method = lambda self: "Calling Method..."
print(y.method())
print(hasattr(x, 'attr'))
