# 13_object_of_store.py
import simpy
import random

NUM_VEHICLES = 50


class Vehicle:
    brands = ["Chevrolet", "Suzuki", "Mazda", "Subaru"]

    def __init__(self, brand):
        self.brand = brand


def productor(env, store):
    for i in range(NUM_VEHICLES):
        yield env.timeout(1)
        vehicle = Vehicle(random.choice(Vehicle.brands))
        yield store.put(vehicle)
        print('vehicle {0} added at {1}'.format(vehicle.brand, env.now))


def consummer(name, env, store):
    while True:
        yield env.timeout(5)
        print(name, 'requesting a product at', env.now)
        item = yield store.get(lambda vehicle: vehicle.brand == "Mazda")
        print('{1} vehicle {0} is delivered to consummer at {2}'
              .format(name, item.brand, env.now))

env = simpy.Environment()
tienda = simpy.FilterStore(env, capacity=NUM_VEHICLES)

prod = env.process(productor(env, tienda))
comsumidores = [env.process(consummer(i, env, tienda)) for i in range(10)]

env.run(until=2500)
