def efficient_fib(f):  # recieves a function as an argument
    data = {}

    def func(x):  # this is the new function to be returned
        if x not in data:
            data[x] = f(x)  # the function recieved as an argument
                            #is now called
        return data[x]

    return func

# we use the decorator.
fib = efficient_fib(fib)
# The fib function is now "decorated" by the function
#"efficient_fib"
t1 = datetime.datetime.now()

# We still use the same function name, there is no need
#to call the new function
print(fib(n))
print("Execution time: {}".format(datetime.datetime.now() - t1))
