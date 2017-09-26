# code0.py

import threading
import time


def worker():
    print("{} starting...".format(threading.currentThread().getName()))
    # This stops the thread execution for 2 seconds.
    time.sleep(2)
    print("{} exiting...".format(threading.currentThread().getName()))


def service():
    print("{} starting...".format(threading.currentThread().getName()))
    # This stops the thread execution for 4 seconds.
    time.sleep(4)
    print("{} exiting...".format(threading.currentThread().getName()))


# We create two named threads
t1 = threading.Thread(name='Thread 1', target=service)
w1 = threading.Thread(name='Thread 2', target=worker)

# This uses the default name (Thread-i)
w2 = threading.Thread(target=worker)

# All threads are executed
w1.start()
w2.start()
t1.start()


# The following will be printed before the threads finish executing
print('\nThree threads were created\n')
