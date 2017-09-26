x = [11, 32, 43]
for c in x:
    print(c)
print(x.__iter__)
next(x)  # Lists are not iterators
