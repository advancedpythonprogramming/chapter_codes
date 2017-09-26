def mov_avg():
    print("Entering ...")
    total = float((yield))
    cont = 1
    print("total = {}".format(total))
    while True:
        print("While loop ...")
        # Here i receive the message and also the yield returns total/count
        i = yield total / cont
        cont += 1
        total += i
        print("i = {}".format(i))
        print("total = {}".format(total))
        print("cont = {}".format(cont))


m = mov_avg()
print("Entering to the first next")
next(m)  # We move to the first yield
print("Leaving the first next")
m.send(10)
print("Entering to send(5)")
m.send(5)
print("Entering to send(0)")
m.send(0)
print("Entering to second send(0)")
m.send(0)
print("Entering to send(20)")
m.send(20)