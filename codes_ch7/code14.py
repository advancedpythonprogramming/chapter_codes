# code14.py

import time
import threading


class Producer(threading.Thread):
    # This thread is implemented as a class

    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self):
        # We open the file using a context manager. We explain this in details
        # in Chapter 10.
        with open('raw_numbers.txt') as file:
            for line in file:
                values = tuple(map(int, line.strip().split(',')))
                self.queue.append(values)


def consumer(queue):
    # This thread is implemented as a function

    with open('processed_numbers.txt', 'w') as file:
        while len(queue) > 0:
            numbers = queue.pop()
            file.write('{}\n'.format(sum(numbers)))

            # Simulates that the consumer is slower than the producer
            time.sleep(0.001)


if __name__ == '__main__':

    queue = MyDeque()

    p = Producer(queue)
    p.start()

    c = threading.Thread(target=consumer, args=(queue,))
    c.start()
