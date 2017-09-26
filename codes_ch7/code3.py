# code3.py

import threading
import time


class Worker(threading.Thread):
    
    def __init__(self, t):
        super().__init__()
        self.t = t

    def run(self):
        print("{} starting...".format(threading.currentThread().getName()))
        time.sleep(self.t)
        print("{} exiting...".format(threading.currentThread().getName()))


class Service(threading.Thread):

    def __init__(self, t):
        super().__init__()
        self.t = t

    def run(self):
        print("{} starting...".format(threading.currentThread().getName()))
        time.sleep(self.t)
        print("{} exiting...".format(threading.currentThread().getName()))


# Creating threads
t1 = Service(5)
w1 = Worker(2)
w2 = Worker(4)

# Starting threads
t1.start()
w1.start()
w2.start()

# Here we call the join() method to block the main program.
# The other threads keep running independently 
t0 = time.time()
w1.join()
print('Main program waits for: {}'.format(time.time() - t0))
