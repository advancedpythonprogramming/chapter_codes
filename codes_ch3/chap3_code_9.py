A = [1, 2, 3, 4]
B = ['a', 'b', 'c', 'd']

zipped = zip(A, B)
zipped = list(zipped)
print(zipped)
unzipped = zip(*zipped)
unzipped = list(unzipped)
print(unzipped)
