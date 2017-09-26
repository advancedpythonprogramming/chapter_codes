# 14_MM1.py
import random
import simpy

# RANDOM_SEED = 42   # Include to achieve repeatable results
NUM_MACHINES = 1        # number of washing machines. MM1
WASHING_TIME = 5        # The service time of a machine
ARRIVAL_TIME = 7        # time between arrivals,
# 1 vehicle comes every 7 minutes
SIMULATION_TIME = 20    # simulation time in minutes


class WashingMachine:
    '''
    A washing machine has a limited number of machines. In this example is one.
    The vehicles request resources of the available machine using the request()
    method. Once the resource is assigned, washing starts and should be
    expected to finish in the WASHING_TIME defined.
    '''

    def __init__(self, env, num_machines, washing_time):
        self.env = env
        # Create a Resource with num_machines machines
        self.machines = simpy.Resource(env,
                                       capacity=num_machines)
        self.washing_time = washing_time

    def wash(self, vehicle):
        '''Washing starts with a random time with probability distribution
        exponential with rate 1 / TIEMPO_LAVADO'''

        yield self.env.timeout(round(
            random.expovariate(1 / self.washing_time) + 0.5))


def vehicle(env, vehicle_id, washing_machine):
    '''During washing, a vehicle arrives to machine and asks use. Once you
    start washing, waits until it finishes and then frees the machine.'''

    print('{0} arrives to machine in {1:.2f}.'.format(vehicle_id, env.now))

    with washing_machine.machines.request() as request:
        yield request

        print('{0} enters to machine in {1:.2f}.'
              .format(vehicle_id, env.now))
        yield env.process(washing_machine.wash(vehicle_id))

        print('{0} goes out from machine in {1:.2f}.'
              .format(vehicle_id, env.now))


def sim_configuration(env,  num_machines,
                      washing_time,
                      arrival_time):
    ''' In this routine: washing machines are created, an initial number of
    vehicles (2) and then vehicles arrive at a rate of 1 / arrival_time'''

    # Create a washing machine
    machine = WashingMachine(env, num_machines, washing_time)

    # 2 vehicles are created and put in to the queue
    print('In the queue there are already 2 vehicles')
    for i in range(2):
        env.process(vehicle(env, 'Vehicle {0}'.format(i), machine))

    # While the machine runs vehicles arrive at a rate of 1 / arrival_time
    while True:
        yield env.timeout(round(random.expovariate(1 / arrival_time)))
        i += 1
        env.process(vehicle(env, 'Vehicle {0}'.format(i), machine))


# Simulation configuration
# random.seed(RANDOM_SEED)

# Simulation environment creation
env = simpy.Environment()
env.process(sim_configuration(env,  NUM_MACHINES,
                              WASHING_TIME,
                              ARRIVAL_TIME))

# Runs simulation until SIMULATION_TIME minutes
env.run(until=SIMULATION_TIME)
