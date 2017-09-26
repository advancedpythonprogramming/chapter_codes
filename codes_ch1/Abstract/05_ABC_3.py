# 05_ABC_3.py

from abc import ABCMeta, abstractmethod


class Base(metaclass=ABCMeta):
    @abstractmethod
    def func_1(self):
        pass

    @abstractmethod
    def func_2(self):
        pass


class SubClass(Base):
    
    def func_1(self):
        pass

    def func_2(self):
        pass

    # We forgot again to implement func_2

c = SubClass()
print('Subclass: {}'.format(issubclass(SubClass, Base)))
print('Instance: {}'.format(isinstance(SubClass(), Base)))