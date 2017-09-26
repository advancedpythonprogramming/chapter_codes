from collections import deque

# We create an empty deque and item by item
d = deque()
d.append('r')
d.append('a')
d.append('d')
d.append('a')
d.append('r')
d.append('e')
d.append('s')

print(d)
print(len(d))

# Next, we check the first and the last items
print(d[0], d[-1])

# Then, we rotate the deque in k=3 step
d.rotate(3)
print(d)

# Finally, we extract the first and the last items
first = d.popleft()
last = d.pop()

print(first, last)
print(d)
