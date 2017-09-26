from collections import namedtuple

def compute_geometry(a, b):  
    Features = namedtuple('Geometrical', 'area perimeter mpa mpb')
    area = a*b
    perimeter = (2*a) + (2*b)
    mpa = a/2
    mpb = b/2
    return Features(area, perimeter, mpa, mpb)

data = compute_geometry(20.0, 10.0)
print(data.area)
