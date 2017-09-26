# code5.py

import threading
import time
import logging


# This sets ups the format in which the messages will be logged on console
logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s]'
                                        '(%(threadName)-10s) %(message)s')

class Worker(threading.Thread):
    
    def __init__(self, t):
        super().__init__()
        self.t = t

    def run(self):
        logging.debug('Starting')
        time.sleep(self.t)
        logging.debug('Exiting')


class Service(threading.Thread):

    def __init__(self, t):
        super().__init__()
        self.t = t

    def run(self):
        logging.debug('Starting')
        time.sleep(self.t)
        logging.debug('Exiting')


# Creating threads
t1 = Service(4)
w1 = Worker(2)
w2 = Worker(2)

# Starting threads
w1.start()
w2.start()
t1.start()

