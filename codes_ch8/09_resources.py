# 09_resources.py
import simpy
import random


def user_resource(env, resource):
        # generates a new request event
    device = resource.request()
    # waits for a resource
    yield device
    # generate task execution time
    yield env.timeout(random.randint(5, 10))
    print('Resource used for {0} minutes'.format(env.now))
    # release the resource
    resource.release(device)

env = simpy.Environment()
res = simpy.Resource(env, capacity=1)
user = env.process(user_resource(env, res))
env.run()
