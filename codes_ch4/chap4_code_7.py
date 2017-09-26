def create_class(name, attr_name, attr_value):
    return type(name, (), {attr_name: attr_value})

Body = create_class("Body", "weight", 100)
bd = Body()  # using it as a normal class to create instances.
print(bd.weight)
