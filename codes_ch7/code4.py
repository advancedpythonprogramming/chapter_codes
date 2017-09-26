# code4.py

import threading
import time


class Service(threading.Thread):

    def __init__(self, t):
        super().__init__()
        self.t = t

    def run(self):
        print("{} starting...".format(threading.currentThread().getName()))
        time.sleep(self.t)
        print("{} exiting...".format(threading.currentThread().getName()))


t = Service(4)
t.start()

# The main program will wait 5 seconds after 't' has finished executing
# before continuing its execution.
t.join(5)

# This returns true if the thread is not currently executing
if not t.isAlive():
    print('The thread has finished successfully')
else:
    print('The thread is still executing')
