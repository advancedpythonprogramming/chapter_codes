# code13.py

import collections
import threading

class MyDeque(collections.deque):

    # We inherit from a normal collections module Deque and
    # we add the locking mechanisms to ensure thread
    # synchronization

    def __init__(self):
        super().__init__()
        # A lock is created for this queue
        self.lock = threading.Lock()

    def append(self, element):

        # The lock is used within a context manager
        with self.lock:
            super().append(element)
            print('[ADD] queue now has {} elements'.format(len(self)))

    def popleft(self):
        with self.lock:
            print('[REMOVE] queue now has {} elements'.format(len(self)))
            return super().popleft()
