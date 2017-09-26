from sys import getsizeof

# using parenthesis indicates that we are creating a generator
a = (b for b in range(10))

print(getsizeof(a))

c = [b for b in range(10)]

# c uses more memory than a
print(getsizeof(c))

for b in a:
    print(b)

print(sum(a)) # the sequence has disappeared
