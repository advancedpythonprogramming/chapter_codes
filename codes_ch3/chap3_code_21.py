def dec_count(n):
    print("Counting down from {}".format(n))
    while n > 0:
        yield n
        n -= 1