from collections import defaultdict

num_items = 0

def my_function():
    global num_items
    num_items += 1
    return ([str(num_items)])

d = defaultdict(my_function)

print(d['a'])
print(d['b'])
print(d['c'])
print(d['d'])
print(d)
