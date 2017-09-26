# code7_1.py

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

# Executing threads
w1.start()
t1.start()
