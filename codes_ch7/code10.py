# code10.py

import threading

def delayed_message(msg):
    print("Message:", msg)

t1 = threading.Timer(10.0, delayed_message, args=("This is a thread t1!",))
t2 = threading.Timer(5.0, delayed_message, args=('This is a thread t2!',))
t3 = threading.Timer(15.0, delayed_message, args=('This is a thread t3!',))

# This thread will start after 10 seconds
t1.start()

# This thread will start after 5 seconds
t2.start()

# Here we cancel thread t1
t1.cancel()

# This thread will start after 15 seconds
t3.start()


