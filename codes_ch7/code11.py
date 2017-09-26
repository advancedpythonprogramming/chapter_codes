# code11.py

import threading


# This class models a thread that blocks to a file
class MyThread(threading.Thread):
    
    lock = threading.Lock()

    def __init__(self, i, file):
        super().__init__()
        self.i = i
        self.file = file

    # This method is the one executed when the start() method is called.
    def run(self):
        
        # Blocks other threads from entering the next block
        MyThread.lock.acquire()
        try:
            self.file.write('This line was written by thread #{}\n'.format(self.i))
        finally:
            # Releases the resource
            MyThread.lock.release()


if __name__ == '__main__':
    n_threads = 15
    threads = []

    # We create a file to write the output.
    with open('out.txt', 'w') as file:

        # All writing threads are created at once
        for i in range(n_threads):
            
            my_thread = MyThread(i, file)

            # The thread is started, which executes the run() method.
            my_thread.start()
            threads.append(my_thread)