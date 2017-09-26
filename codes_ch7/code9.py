# code9.py

import threading
import logging
import time

logging.basicConfig(level=logging.DEBUG,format='(%(threadName)-10s) '
                                                            '%(message)s')

class DaemonThread(threading.Thread):
    
    def __init__(self, t):
        super().__init__()
        self.t = t
        self.daemon = True
        self.name = 'daemon'
    
    def run(self):
        logging.debug('Starting')
        time.sleep(self.t)
        logging.debug('Exiting')

class NonDaemonThread(threading.Thread):
    
    def __init__(self, t):
        super().__init__()
        self.t = t
        self.name = 'non-daemon'

    def run(self):
        logging.debug('Starting')
        time.sleep(self.t)
        logging.debug('Exiting')

# Creating threads
d = DaemonThread(3)
t = NonDaemonThread(1)

# Executing threads
d.start()
t.start()

# Waiting thread d for 1 seconds 
d.join(2)
print('is d alive?: {}'.format(d.isAlive()))
