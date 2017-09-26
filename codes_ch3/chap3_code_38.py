@memoize(0.0001)
def complex_process(a, b):
    return a + b

# This is the same as calling
# complex_process = memoize(0.0001)(complex_process)
# after defining the function

print(complex_process(2, 2))
print(complex_process(2, 1))
print(complex_process(2, 2))
print(complex_process(2, 2))
print(complex_process(2, 2))
print(complex_process(2, 2))
print(complex_process(2, 2))
print(complex_process(2, 2))
print(complex_process(2, 2))  