a_list = [1, 2, 3, 4, 5, 6]


class MySequence:
    # given that we are not overriding the __reversed__ method, the built-in
    # will be used (iterating with __getitem__ and __len___)
    def __len__(self):
        return 9

    def __getitem__(self, index):
        return "Item_{0}".format(index)


class MyReversed(MySequence):
    def __reversed__(self):
        return "Reversing!!"


for seq in a_list, MySequence(), MyReversed():
    print("\n{} : ".format(seq.__class__.__name__), end="")
    for item in reversed(seq):
        print(item, end=", ")
