from collections import defaultdict


class MyList(list):
    def __len__(self):
        # Each time this method is called with a non-existing key, the
        # key-value pair is generated with a default value of 0
        d = defaultdict(int)
        # This value comes from calling "int" without arguments. (Try
        # typing int() on Python's console)

        # Here we call the original method from the super-class list
        for i in range(list.__len__(self)):
            d.update({self[i]: d[self[i]] + 1})

        # Here we call d's (a defaultdict) len method
        return len(d)


L = MyList([1, 2, 3, 4, 5, 6, 6, 7, 7, 7, 7, 2, 2, 3, 3, 1, 1])
print(len(L))
