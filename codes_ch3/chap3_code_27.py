def grep(pattern):
    print("Searching for %s" % pattern)
    while True:
        line = yield
        if pattern in line:
            print(line)


o = grep("Hello")  # creating the object won't execute the function yet
next(o)  # Move on to the first yield, "Searching for ..." will be printed

o.send("This line contains Hello")
o.send("This line won't be printed")
o.send("This line will (because it contains Hello :) )")
o.send("This line won't be shown either")
