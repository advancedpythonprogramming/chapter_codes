# 03_ABC_1.py

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

    # We intentionally did not implement func_2

print('Is it subclass?: {}'.format(issubclass(SubClass, Base)))
print('Is it instance?: {}'.format(isinstance(SubClass(), Base)))
