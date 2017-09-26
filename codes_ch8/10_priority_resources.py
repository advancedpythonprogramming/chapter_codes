# 10_priority_resources.py
import simpy
import random


class Client:

    def __init__(self, c_id, env, resource, waiting_time, priority):
        self.env = env
        self.resource = resource

        self.id_client = c_id
        self.waiting_time = waiting_time
        self.priority = priority
        self.action = self.env.process(self.run())

    def run(self):
        # Without "while" loop the client is a unique entity
        yield self.env.timeout(self.waiting_time)

        with self.resource.request(priority=self.priority) as req:
            print('client {} is asking for a resource at time={}. Priority={}.'
                  .format(self.id_client, self.env.now, self.priority))
            yield req
            print('client {} obtains a resource at time={}'
                  .format(self.id_client, self.env.now))
            yield self.env.timeout(3)

env = simpy.Environment()
res = simpy.PriorityResource(env, capacity=1)
c1 = Client(1, env, res, waiting_time=0, priority=0)
c2 = Client(2, env, res, waiting_time=1, priority=0)
c3 = Client(3, env, res, waiting_time=2, priority=-1)
env.run()
