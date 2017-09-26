class Test:

    def __call__(self, *args, **kwargs):
        print(args)
        print(kwargs)
        print('-' * 40)

t = Test()
t(1, 2, 3)
t(a=1, b=2, c=3)
t(4, 5, 6, d=4, e=5, f=6)
