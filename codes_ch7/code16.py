# code16.py

import threading
import time
import queue


class Producer(threading.Thread):

    def __init__(self, que):
        super().__init__()
        self.que = que

    def run(self):
        with open('raw_numbers.txt') as file:
            for line in file:
                values = tuple([int(l) for l in line.strip().split(',')])
                self.que.put(values)
                print('[PRODUCER] The queue has {} elements.'.format( \
                    self.que.qsize()))

                # Simulates a slower process
                time.sleep(0.001)


def consumer(que):
    with open('processed_numbers.txt', 'w') as file:
        while True:

            # A try/except clause is used in order to stop
            # the consumer once there is no elements left in the
            # queue. If not for this, the consumer would be executing
            # for ever

            try:

                # If no elements are left in the queue, an Empty
                # exception is raised
                numbers = que.get(False)
            except queue.Empty:
                break
            else:
                file.write('{}\n'.format(sum(numbers)))
                que.task_done()

                # qsize() returns the queue size
                print('[CONSUMER] The queue now has {} elements.'.format( \
                    que.qsize()))

                # Simulates a complex process. If the consumer was faster 
                # than the producer, the threads would end abruptly
                time.sleep(0.005)


if __name__ == '__main__':

    q = queue.Queue()

    # a producer is created and executed
    p = Producer(q)
    p.start()

    # a consumer thread is created and executed with the same queue
    c = threading.Thread(target=consumer, args=(q,))
    c.start()
