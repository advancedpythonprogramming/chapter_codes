# We can take a slice
numbers = [6,7,2,4,10,20,25]
print(numbers[2:6])

# We can pick a portion until the end
print(numbers[2::])

# We can take a slice from the beginning until a specific position
print(numbers[:5])

# We can also change the number of steps
print(numbers[:5:2])

# We can revert a list
print(numbers[::-1])
