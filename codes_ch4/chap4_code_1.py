class ObjectCreator:
    pass

print(ObjectCreator)


def visualize(o):
    print(o)

visualize(ObjectCreator)

# Here we check if ObjectCreator has the attribute weight
print(hasattr(ObjectCreator, 'weight'))

# Here we are directly adding the weight attribute
ObjectCreator.weight = 80
print(hasattr(ObjectCreator, 'weight'))
print(ObjectCreator.weight)

# Assigning the class to a new variable
# Note that both variables reference the same object
ObjectCreatorMirror = ObjectCreator  
print(id(ObjectCreatorMirror))
print(id(ObjectCreator))
print(ObjectCreatorMirror.weight)
