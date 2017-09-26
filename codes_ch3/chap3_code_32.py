from functools import reduce
import datetime

reduce(lambda x, y: x + y, range(1, 10))

# Lets compute the length of a file's longest line
# rstrip returns a string copy that has no trailing spaces
#(or the character specified)
# eg: "Hello...".rstrip(".") returns "Hello"

t = datetime.datetime.now()
r1 = reduce(max, map(lambda l: len(l.rstrip()), [line for line
                                                 in open('logs_out.txt')]))
print("reduce time: {}".format(datetime.datetime.now() - t))
print(r1)

# Another way of doing the same with generator comprehensions and numpy
t = datetime.datetime.now()
r2 = max((len(line.rstrip()) for line in open('logs_out.txt')))
print("max(generator) time: {}".format(datetime.datetime.now() - t))
print(r2)

# To visualize the lines of the file
for line in open('logs_out.txt'):
    print(line.rstrip())
