# 02_DES.py

from collections import deque
from random import choice
from random import expovariate


class Vehicle:
    """
    This class represent vehicles wich arrives to
    the mechanical workshop
    """

    def __init__(self, arrival_time=0):
        self.vehicle_type = choice(['motorcycle', 'pickup_truck', 'car'])
        self.arrival_time = arrival_time

    def __repr__(self):
        return 'Vehicle type: {0}'.format(self.vehicle_type)


class WorkShop:
    def __init__(self, types):
        self.current_task = None
        self.review_time = 0
        self.types = types

    def pass_vehicle(self, vehicle):
        self.current_task = vehicle
        # Create a randon review time
        current_type_rate = self.types[vehicle.vehicle_type]
        self.review_time = round(expovariate(current_type_rate))

    @property
    def busy(self):
        return self.current_task is not None


class Simulation:
    """
    This class implements the simulation.
    Also you can use a function like in the previous case.
    All variables used in the simulation are initialized.
    """

    def __init__(self, maximum_time, arrival_rate, types):
        self.maximum_sim_time = maximum_time
        self.arrival_rate = arrival_rate
        self.simulation_time = 0
        self.next_vehicle_time = 0
        self.final_service_time = float('Inf')
        self.waiting_time = 0
        self.workshop = WorkShop(types)
        self.waiting_line = deque()
        self.served_vehicles = 0

    def next_vehicle(self, arrival_rate):
        # update the arrival time of the next vehicle
        self.next_vehicle_time = self.simulation_time + \
                                 round(expovariate(arrival_rate))

    def run(self):
        """
        This method executes the simulation of the
        workshop and the waiting line

        """
        self.next_vehicle(self.arrival_rate)

        # The cycle is executed verified the simulation time is less than
        # maximum simulation time
        while self.simulation_time < self.maximum_sim_time:

            # Cambiar esta condicion con un if que sea compatible con el uso
            # del taller y que reemplace hacer inf el tiempo de servicio.
            # Update simulation time
            self.simulation_time = min(self.next_vehicle_time,
                                       self.final_service_time)
            print('[SIMULATION] time = {0} min'.format(self.simulation_time))

            # First, review the next event between arrival and the final of a
            # service

            if self.simulation_time == self.next_vehicle_time:

                # If a vehicle has arrived
                # we have to put in to the queue
                self.waiting_line.append(Vehicle(self.simulation_time))

                # If a vehicle has arrived we have to generate the next arrival
                self.next_vehicle(self.arrival_rate)

                print('[QUEUE] {0} arrives in: {1} min.'.format(
                    self.waiting_line[-1].vehicle_type,
                    self.simulation_time))

                # If the workshop is busy, the vehicle has to wait for its
                # turn, else can be served

                if not self.workshop.busy:
                    # Get the next vehicle in the waiting line
                    next_vehicle = self.waiting_line.popleft()

                    # The vehicle begin to be served
                    self.workshop.pass_vehicle(next_vehicle)

                    # Update the waiting time, added 0 actually
                    self.waiting_time += self.simulation_time \
                                         - self.workshop.current_task.arrival_time

                    # The next final time is generated
                    self.final_service_time = self.simulation_time \
                                              + self.workshop.review_time

                    # Update counter of served vehicles
                    self.served_vehicles += 1

                    print('[W_SHOP] {0} enters with a expected service time {'
                          '1} min.'.format(
                        self.workshop.current_task.vehicle_type,
                        self.workshop.review_time))

            elif self.simulation_time == self.final_service_time:

                print('[W_SHOP] Departure: {0} at {1} min.'.format(
                    self.workshop.current_task.vehicle_type,
                    self.simulation_time))

                if len(self.waiting_line) == 0:
                    # We make sure that simulation time is next_vehicle_time
                    self.final_service_time = float('Inf')
                    self.workshop.current_task = None

                else:
                    # Get the next vehicle in the waiting line
                    next_vehicle = self.waiting_line.popleft()

                    # The vehicle begin to be served
                    self.workshop.pass_vehicle(next_vehicle)

                    # Update the waiting time
                    self.waiting_time += self.simulation_time - \
                                         self.workshop.current_task.arrival_time

                    # The next final service time is updated
                    self.final_service_time = self.simulation_time \
                                              + self.workshop.review_time

                self.served_vehicles += 1

        print('Statistics:')
        print('Total service time {0} min.'.format(self.final_service_time))
        print('Total number of served vehicles: {0}'
              .format(self.served_vehicles))
        w_time = self.waiting_time / self.served_vehicles
        print('Average waiting time {0} min.'.format(round(w_time)))


if __name__ == '__main__':
    # Set the arrival rate in 5 minutes.
    arrival_rate_vehicles = 1 / 5

    # Here we define different types of vehicles and the their service time.
    vehicles = {'motorcycle': 1.0 / 8, 'car': 1.0 / 15,
                'pickup_truck': 1.0 / 20}

    # The simulation runs until 50 minutes.
    s = Simulation(50, arrival_rate_vehicles, vehicles)
    s.run()
