# Yet another way
class MyList3(list):
    def __len__(self):
        d = set(self)
        return len(d)

L = MyList3([1, 2, 3, 4, 5, 6, 6, 7, 7, 7, 7, 2, 2, 3, 3, 1, 1])
print(len(L))
