# 01_synchronous.py

from collections import deque
import random


class Vehicle:
    """
    This class represent vehicles which arrives to the mechanical 
    workshop
    """

    def __init__(self, vehicles):
        # When a new vehicle is created is chosen randomly incoming 
        # vehicle type and the average time of service'''

        self.vehicle_type = random.choice(list(vehicles))
        self._review_time = round(
            random.expovariate(vehicles[self.vehicle_type]))

    @property
    def review_time(self):
        return self._review_time

    @review_time.setter
    def review_time(self, value):
        self._review_time = value

    def show_type(self):
        print("Being treated: {0} with an average time of {1} minutes"
              .format(self.vehicle_type, self.review_time))


class WorkShop:
    """
    This class represent the review line in the workshop.
    """

    def __init__(self):
        self.current_task = None
        self.review_time = 0

    def busy(self):
        return self.current_task is not None

    def next_vehicle(self, vehicle):
        self.current_task = vehicle
        self.review_time = vehicle.review_time
        vehicle.show_type()

    def tick(self):
        if self.current_task is not None:
            self.review_time -= 1
            if self.review_time <= 0:
                self.current_task = None


def new_vehicle_arrive():
    """
    This function returns if arrive a new vehicle to queue. It is
    sampled from a uniform probability distribution. The method
    returns True if the value delivered by the random function is
    greater than a given value.
    """
    return random.random() >= 0.8


def technical_workshop(max_time, vehicles):
    """
     This function handles the process or technical service.
    """

    # Fix the random seed
    random.seed(10)

    # A WorkShop is created
    workshop = WorkShop()

    # Empty review line
    review_line = deque()

    # Waiting time
    waiting_times = []

    # The simulation cycle is defined until the maximum time in
    # minutes, each time t is increased is evaluated if a new
    # vehicle arrives at the review queue

    for t in range(max_time):
        if new_vehicle_arrive():
            review_line.append(Vehicle(vehicles))

        if not workshop.busy() and len(review_line) > 0:
            # Next vehicle is taken out from review queue
            curr_vehicle = review_line.popleft()
            waiting_times.append(curr_vehicle.review_time)
            workshop.next_vehicle(curr_vehicle)

        # Decrease one tick of time to waiting vehicle
        workshop.tick()

    average_time = sum(waiting_times) / len(waiting_times)
    total_time = sum(waiting_times)
    print('Statistics:')
    print('Average waiting time {0:6.2f} min.'.format(average_time))
    print('Total workshop service time was', '{0:6.2f} min'.format(
        total_time))
    print('Total vehicles serviced: {0}'.format(len(waiting_times)))


if __name__ == '__main__':

    # The types of vehicles and the average service time are defined
    vehicles = {'motorcycle': 1.0 / 8, 'car': 1.0 / 15,
                'pickup_truck': 1.0 / 20}
    maximum_time = 200
    technical_workshop(maximum_time, vehicles)
