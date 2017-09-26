# We create the list with seven numbers
numbers = [6, 7, 2, 4, 10, 20, 25]
print(numbers)

# Ascendence. Note that variable a do not receive
# any value from assignation.
a = numbers.sort()
print(numbers, a)

# Descendent
numbers.sort(reverse=True)
print(numbers)
