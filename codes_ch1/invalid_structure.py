# invalid_structure.py

class X():
    def call_me(self):
        print("I'm X")


class Y():
    def call_me(self):
        print("I'm Y")


class A(X, Y):
    def call_me(self):
        print("I'm A")


class B(Y, X):
    def call_me(self):
        print("I'm B")


class F(A, B):
    def call_me(self):
        print("I'm F")

# TypeError: Cannot create a consistent method resolution
# order (MRO) for bases X, Y
