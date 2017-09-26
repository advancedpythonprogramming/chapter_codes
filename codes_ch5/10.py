# 10.py


class Circle:

    def __init__(self, center):
        if not isinstance(center, tuple):
            raise Exception('Center has to be a tuple')
            print('This line is not printed')

        self.center = center

    def __repr__(self):
        return 'The center is {0}'.format(self.center)


c1 = Circle((2, 3))
print(c1)

c2 = Circle([2, 3])
print(c2)
