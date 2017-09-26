# diamond_problem.py

class ClassB:
    num_calls_B = 0

    def make_a_call(self):
        print("Calling method in ClassB")
        self.num_calls_B += 1


class LeftSubClass(ClassB):
    num_left_calls = 0

    def make_a_call(self):
        ClassB.make_a_call(self)
        print("Calling method in LeftSubClass")
        self.num_left_calls += 1


class RightSubClass(ClassB):
    num_right_calls = 0

    def make_a_call(self):
        ClassB.make_a_call(self)
        print("Calling method in RightSubClass")
        self.num_right_calls += 1


class SubClassA(LeftSubClass, RightSubClass):
    num_calls_subA = 0

    def make_a_call(self):
        LeftSubClass.make_a_call(self)
        RightSubClass.make_a_call(self)
        print("Calling method in SubClassA")
        self.num_calls_subA += 1


if __name__ == '__main__':
    s = SubClassA()
    s.make_a_call()
    print("SubClassA: {}".format(s.num_calls_subA))
    print("LeftSubClass: {}".format(s.num_left_calls))
    print("RightSubClass: {}".format(s.num_right_calls))
    print("ClassB: {}".format(s.num_calls_B))
