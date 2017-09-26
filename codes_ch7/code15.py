# code15.py

import threading


class FirstProcess(threading.Thread):

    def __init__(self, lock_a, lock_b):
        self.lock_a = lock_a
        self.lock_b = lock_b

    def run(self):
        with self.lock_a:
            # Acquire the first lock

            with self.lock_b:
            # Acquire the second lock for another concurrent task


class SecondProcess(threading.Thread):
        
    def __init__(self, lock_a, lock_b):
        self.lock_a = lock_a
        self.lock_b = lock_b

    def run(self):
        with self.lock_b:
            # Acquire the first lock
            # Notice that this thread require the lock_b, that
            # could be taken fot other thread previously

            with self.lock_a:
                # Acquire the second lock for another concurrent task


lock_a = threading.Lock()
lock_b = threading.Lock()

t1 = FirstProcess(lock_a, lock_b)
t2 = SecondProcess(lock_a, lock_b)
t1.start()
t2.start()