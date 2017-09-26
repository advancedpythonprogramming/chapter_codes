# Create an empty Stack. In Python Stacks are built-in as Lists.
stack = []

# push() method
stack.append(1)
stack.append(10)
stack.append(12)

print(stack)

# pop() method
stack.pop()
print('pop(): {0}'.format(stack))

# top() method. Lists does not have a this method implemented directly.
#We can have the same behaviour indexing the last element in the Stack.
stack.append(25)
print('top(): {0}'.format(stack[-1]))

# len()
print('The stack have {0} elements'.format(len(stack)))

# is_empty() method. In Python we verify the status of the stack
#checking if it has elements.
stack  = []
if len(stack) == 0:
    print('The stack is empty :(')
