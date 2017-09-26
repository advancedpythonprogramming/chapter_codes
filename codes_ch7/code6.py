# code6.py

import threading
import logging
import time

logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-10s)'
                                                        ' %(message)s')

def daemon():
    logging.debug('Starting')
    time.sleep(4)
    logging.debug('Exiting')

d1 = threading.Thread(name='daemon', target=daemon)

# We set d1 as a daemon
d1.setDaemon(True)

def non_daemon():
    logging.debug('Starting')
    logging.debug('Exiting')

t1 = threading.Thread(name='non-daemon', target=non_daemon)

d1.start()
t1.start()
