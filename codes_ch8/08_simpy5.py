# 08_simpy5.py
import simpy
import random


def waiter(env, kitchen):
    # the time at which the preparation is interrupted
    yield env.timeout(5)
    # We use the interrupt () method of cooking process
    kitchen.action.interrupt()


class Kitchen:

    def __init__(self, env):
        self.env = env
        self.action = env.process(self.run())

    def run(self):
        while True:
            print('A dish begins to be prepared t={0}'.format(self.env.now))

            try:
                yield self.env.process(self.preparation())
            except simpy.Interrupt:
                # If the preparation of the dish takes more time than the
                # permitted delay time should be discontinued and go to the
                # next stage
                print('[WAITER] the preparation takes a',
                      'long time, place in the oven as it is')

            print('A dish is put in the oven t={0}'.format(self.env.now))
            cooking_time = random.randint(5, 10)
            yield self.env.timeout(cooking_time)

    def preparation(self):
        yield self.env.timeout(random.randint(5, 20))

maximum_time = 80

env = simpy.Environment()
k = Kitchen(env)
env.process(waiter(env, k))  # waiter activated
env.run(until=maximum_time)
