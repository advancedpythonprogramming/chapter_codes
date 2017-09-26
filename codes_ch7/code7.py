# code7.py

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
        # We can set a thread as deamon inside the class definition
        # setting the daemon attribute as True
        self.daemon = True

    def run(self):
        print("{} starting...".format(threading.currentThread().getName()))
        time.sleep(self.t)
        print("{} exiting...".format(threading.currentThread().getName()))


# Creating threads
t1 = Service(5)
w1 = Worker(2)

# Setting the working thread as daemon
# We can use this same method when we define a function as target 
# of a thread. 
w1.setDaemon(True)

# Executing threads
w1.start()
t1.start()
