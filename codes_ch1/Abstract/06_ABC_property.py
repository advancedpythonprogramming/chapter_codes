# 06_ABC_property.py

from abc import abstractproperty

class Base(metaclass= ABCMeta):
    
    @abstractproperty
    def value(self):
        return 'It shouldn\'t print this'


class Implementation(Base):
    
    @property
    def value(self):
        return 'concrete property'

try:
    b = Base()
    print('Base.value: {}'.format(b.value))
    
except Exception as err:
    print('ERROR: {}'.format(str(err)))

i = Implementation()

print('Implementation.value: {}'.format(i.value))