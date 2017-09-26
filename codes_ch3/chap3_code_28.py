strings = ["ZZ", "YY", "bb", "aa"]
print("Simple sort:", sorted(strings))

# If we want to sort according to the lowercase values:
def lower(s):
    return s.lower()

print("Lower sort: ", sorted(strings, key=lower))

# The same result can be achieved with a lambda function:
print("Lambda sort:", sorted(strings, key=lambda s: s.lower()))
