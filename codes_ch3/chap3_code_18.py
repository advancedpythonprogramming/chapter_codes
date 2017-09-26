import itertools

letters = ['a', 'b', 'c', 'd', 'e', 'f']
bools = [1, 0, 1, 0, 0, 1]
nums = [23, 20, 44, 32, 7, 12]
decimals = [0.1, 0.7, 0.4, 0.4, 0.5]

# Iterates indefinitely over letters.
colors = itertools.cycle(letters)
print(next(colors))
print(next(colors))
print(next(colors))
print(next(colors))
print(next(colors))
print(next(colors))
print(next(colors))
print(next(colors))
print(next(colors))
print(next(colors))

# Iterates across all the iterables in the arguments consecutively.
for i in itertools.chain(letters, bools, decimals):
    print(i, end=" ")

# Iterates over the elements in letters according to the condition in bools.
for i in itertools.compress(letters, bools):
    print(i, end=" ")
