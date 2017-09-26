import numpy as np

def maximum(values):
    temp_max = -np.infty
    for v in values:
        if v > temp_max:
            temp_max = v
        yield temp_max

elements = [10, 14, 7, 9, 12, 19, 33]
res = maximum(elements)
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))  # we've run out of list elements!
