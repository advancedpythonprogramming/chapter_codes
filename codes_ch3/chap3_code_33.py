import datetime


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


n = 35
t1 = datetime.datetime.now()
print(fib(n))
print("Execution time: {}".format(datetime.datetime.now() - t1))
