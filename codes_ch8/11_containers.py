# 11_containers.py
import simpy
import random


class WareHouse:

    def __init__(self, env):
        self.sellers = simpy.Resource(env, capacity=2)
        self.stock = simpy.Container(env, init=100, capacity=1000)
        self.process = env.process(self.warehouse_monitor(env))

    def warehouse_monitor(self, env):
        while True:
            if self.stock.level < 100:
                print('Order supplies at {0}'.format(env.now))
                env.process(truck(env, self))
            yield env.timeout(random.uniform(1, 15))


def truck(env, warehouse):
    # arrival time
    yield env.timeout(random.uniform(1, 10))
    print('Truck arrives at {0}'.format(env.now))
    # the truck provide until the warehouse is full
    quantity = warehouse.stock.capacity - warehouse.stock.level
    yield warehouse.stock.put(quantity)
    print('Truck provided {0} items'.format(quantity))


def client(id, env, warehouse):
    print('Client {0} is arriving at {1}'.format(id, env.now))
    with warehouse.sellers.request() as req:
        yield req
        quantity = 40
        print('Client {0} buys {1} items at {2}'.format(id, quantity, env.now))
        yield warehouse.stock.get(quantity)
        yield env.timeout(random.uniform(1, 5))
        print('Client {0} ends buy at {1}'.format(id, env.now))


def clients_generator(env, warehouse):
    for i in range(4):
        env.process(client(i, env, warehouse))
        yield env.timeout(random.uniform(1, 5))

env = simpy.Environment()
warehouse = WareHouse(env)
car_gen = env.process(clients_generator(env, warehouse))
env.run(until=35)
