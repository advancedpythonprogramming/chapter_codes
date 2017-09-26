f = fibonacci() # Defined before
fib = [next(f) for i in range(11)]
odds = list(filter(lambda x: x % 2 != 0, fib))
print("Odd:", odds)

even = list(filter(lambda x: x % 2 == 0, fib))
print("Even:", even)
