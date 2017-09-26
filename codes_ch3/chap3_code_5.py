class MyClass:
    def __init__(self, word=None):
        self.word = word

    def __getitem__(self, i):
        return self.word[i]


p = MyClass("Hello World")
print(p[0])

[print(c) for c in p]

(a, b, c, d) = p[0:4]
print(a, b, c, d)
print(list(p))
print(tuple(p))
