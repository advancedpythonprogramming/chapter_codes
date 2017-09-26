# 03_simpy0.py

import random
import simpy


def Process(env):
    while True:
        yield env.timeout(random.expovariate(1 / 5))
        print('current time = {0}'.format(env.now))

env = simpy.Environment()
p = env.process(Process(env))
env.run(until=30)
