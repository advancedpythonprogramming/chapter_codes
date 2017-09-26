# 01_abstract_1.py

class Base:
    def func_1(self):
        raise NotImplementedError()

    def func_2(self):
        raise NotImplementedError()
        
class SubClass(Base):
    def func_1(self):
        print("func_1() called...")
        return

    # We intentionally did not implement func_2
    
b1 = Base()
b2 = SubClass()
b2.func_1()
b2.func_2()
