# code1.py

import threading
import time


def worker(t):
    print("{} starting...".format(threading.currentThread().getName()))

    # Thread is stopped for t seconds
    time.sleep(t)
    print("{} exiting...".format(threading.currentThread().getName()))


# Threads are created using the Thread class, these are associated with the
# objective function to be executed by the thread. Function attributes are 
# given using the 'args' keyword. In this example, we only need to give one
# argument. For this reason a one value tuple is given.

w = threading.Thread(name='Thread 2', target=worker, args=(3,))
w.start()