# code8.py

import threading
import logging
import time

logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-10s)'
                                                        ' %(message)s')

class DaemonThread(threading.Thread):
    
    def __init__(self, t):
        super().__init__()
        self.t = t
        self.daemon = True
    
    def run(self):
        logging.debug('Starting')
        time.sleep(self.t)
        logging.debug('Exiting')


class NonDaemonThread(threading.Thread):
    
    def __init__(self, t):
        super().__init__()
        self.t = t
        self.daemon = True
    
    def run(self):
        logging.debug('Starting')
        time.sleep(self.t)
        logging.debug('Exiting')

# Creating threads
d = DaemonThread(2)
t = NonDaemonThread(1)

# Executing threads
d.start()
t.start()

# Waiting for the threads finish
d.join()
t.join()
