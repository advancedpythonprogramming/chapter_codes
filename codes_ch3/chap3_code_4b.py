from collections import defaultdict

# Another way of achieving the same behaviour
class MyList2(list):
    def __len__(self):
        d = defaultdict(int)

        for i in self:  # Here we iterate over the items contained in the object
            d.update({i: d[i] + 1})

        return len(d)


L = MyList2([1, 2, 3, 4, 5, 6, 6, 7, 7, 7, 7, 2, 2, 3, 3, 1, 1])
print(len(L))
