def compute_geometry(a, b):
    area = a * b
    perimeter = (2 * a) + (2 * b)
    mpa = a / 2
    mpb = b / 2

    return (area, perimeter, mpa, mpb)

data = compute_geometry(20.0, 10.0)
print('1: {0}'.format(data))

a = data[0]
print('2: {0}'.format(a))

# Here we unpack the values into independent variables contained
# in the tuple
a, p, mpa, mpb = data
print('3: {0}, {1}, {2}, {3}'.format(a, p, mpa, mpb))
a, p, mpa, mpb = compute_geometry(20.0, 10.0)
print('4: {0}, {1}, {2}, {3}'.format(a, p, mpa, mpb))
