from collections import namedtuple

# name of tuple type (defined by user) and tuple attributes
Register = namedtuple('Register', 'ID_NUMBER name age')
c1 = Register('13427974-5', 'Christian', 20)
c2 = Register('23066987-2', 'Dante', 5)
print(c1.ID_NUMBER)
print(c2.ID_NUMBER)
