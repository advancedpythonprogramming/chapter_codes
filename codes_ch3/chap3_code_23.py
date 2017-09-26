def fibonacci():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b


f = fibonacci()
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
g1 = [next(f) for i in range(10)]
print(g1)
g2 = (next(f) for i in range(10))
for a in g2:
    print(a)
