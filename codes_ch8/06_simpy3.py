# 06_simpy3.py
import simpy
import random


class Kitchen:

    def __init__(self, env):
        # reference to environment
        self.env = env
        # process of the instance
        self.action = env.process(self.run())

    def run(self):
        while True:
            print('A dish begins to be prepared t={0}'.format(self.env.now))

            # the process must wait for the preparation of the dish generate
            # a new event waiting for preparation
            yield self.env.process(self.preparation())

            # cooking the dishes takes a random time between 5 and 10 min
            print('A dish is put in the oven t={0}'.format(self.env.now))
            cooking_time = random.randint(5, 10)
            yield self.env.timeout(cooking_time)

    def preparation(self):
        # prepare each dish takes a random time between 5 and 20 min
        yield self.env.timeout(random.randint(5, 20))

maximum_time = 80

# environment initialized
env = simpy.Environment()
# process added to the environment
k = Kitchen(env)
# simulation run until maximum time
env.run(until=maximum_time)
