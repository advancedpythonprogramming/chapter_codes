# The collection library includes the deque module that manages single queues
# or double ended queues efficiently
from collections import deque

# An empty queue
q = deque()

# We add some elements to the queue using append method, similar to lists.
q.append('orange')
q.append('apple')
q.append('pear')

# Print the queue
print(q)

# We extract the first element and print again the queue
print('Remove the item: {}'.format(q.popleft()))
print(q)

# Add a new element to the queue
q.append('strawberry')

# Get the first element
print('The first item is {}'.format(q[0]))

# len()
print('The queue have {0} elements'.format(len(q)))

# is_empty(). We first remove all the items in the queue using clear() method
# and the we check the number of elements.
q.clear()
if len(q) == 0:
    print('The queue is empty')
