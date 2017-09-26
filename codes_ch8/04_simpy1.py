# 04_simpy1.py
import simpy
import random


class Process:

    def __init__(self, env):
        self.env = env
        self.action = env.process(self.run())

    def run(self):
        # actions executed by the process
        while True:
                # an event is returned by the process
            yield self.env.timeout(random.expovariate(1 / 5))
            print('current time = {0}'.format(self.env.now))


env = simpy.Environment()
p = Process(env)
env.run(until=30)
