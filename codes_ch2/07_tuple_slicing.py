data = (400, 20, 1, 4, 10, 11, 12, 500)
a = data[1:3]
print('1: {0}'.format(a))
a = data[3:]
print('2: {0}'.format(a))
a = data[:5]
print('3: {0}'.format(a))
a = data[2::2]
print('4: {0}'.format(a))
#We can revert a sequence:
a = data[::-1]
print('5: {0}'.format(a))
