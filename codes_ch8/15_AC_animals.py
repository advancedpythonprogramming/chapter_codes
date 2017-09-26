from abc import ABCMeta
from random import expovariate, uniform, choice


class Animal(metaclass=ABCMeta):
    def __init__(self, time):
        # To give an id to each object:
        if not hasattr(self.__class__, 'current_ident'):
            setattr(self.__class__,'current_ident', 0)
        # To keep statistics per class for each simulation
        if time == 0:
            setattr(self.__class__, 'statistics', {
                                'extinction_time': -1,
                                'new_animal': 0,
                                'death_eaten': 0,
                                'death_no_energy': 0,
                                'death_old': 0,
                                'current_num_animals': 0,
                                'time_lived': 0,
                                'time_waited_for_food': 0,
                                'waited_for_food': 0
                                })
        self.ident = self.__class__.current_ident
        self.__class__.current_ident += 1
        self.energy = 50
        self.time_since_hungry = -1
        self._dead = False
        self.moment_of_dead = self.metadata['life_expectancy'] + time
        self.next_eating_time = time
        self.next_new_animal_time = time
        self.set_next_eating_time()
        self.set_next_new_animal_time()
        self.current_time = time
        self.birth_date = time

    @property
    def dead(self):
        return self._dead

    @dead.setter
    def dead(self, value):
        self._dead = value
        self.__class__.statistics['current_num_animals'] -= 1
        if self.__class__.statistics['current_num_animals'] == 0:
            self.__class__.statistics['extinction_time'] = self.current_time
        self.__class__.statistics['time_lived'] += self.current_time - self.birth_date

    def next_action_time(self):
        return min(self.next_new_animal_time, self.moment_of_dead, self.next_eating_time)

    def set_next_eating_time(self, food=True):
        if food:
            param = self.metadata['food_frequency']
            self.next_eating_time += int(uniform(param[0], param[1]))
        else:
            self.next_eating_time += 1

    def set_next_new_animal_time(self):
        self.next_new_animal_time += int(expovariate(self.metadata['new_animal']))

    def eat(self, food, time):
        selected = choice(food)
        # Can eat
        if selected.__class__.__name__ in self.metadata['food']:
            # print("{0}{2} I am eating a {1}{3}".format(self.__class__.__name__, selected.__class__.__name__, self.ident, selected.ident))
            if self.time_since_hungry > 0:
                self.__class__.statistics['time_waited_for_food'] += self.time_since_hungry
                self.__class__.statistics['waited_for_food'] += 1
            self.time_since_hungry = 0
            self.energy += self.metadata['food_energy']
            self.set_next_eating_time()
            selected.die('eaten', time)
        else:
            self.time_since_hungry += 1
            self.set_next_eating_time(False)
            self.energy -= self.metadata['food_energy'] / 2
            if self.energy < 0:
                self.die('energy', time)
            else:
                pass
                # print('{0}{2} Hungry. Found {1}'.format(self.__class__.__name__, selected.__class__.__name__, self.ident))

    def new_animal(self, time):
        self.energy -= self.metadata['new_animal_energy']
        self.set_next_new_animal_time()
        self.__class__.statistics['new_animal'] += 1
        self.__class__.statistics['current_num_animals'] += 1
        # print("Born a new {0} from {1}".format(self.__class__.__name__, self.ident))
        if self.energy == 0:
            self.die('energy', time)

    def die(self, reason, time):
        self.dead = True
        self.current_time = time
        if reason == 'old':
            self.__class__.statistics['death_old'] += 1
        elif reason == 'energy':
            self.__class__.statistics['death_no_energy'] += 1
        elif reason == 'eaten':
            self.__class__.statistics['death_eaten'] += 1

        # print('{0}{2} has died because of {1}'.format(self.__class__.__name__, reason, self.ident))

    def __repr__(self):
        return "{0}{1}".format(self.__class__.__name__, self.ident)


class Tiger(Animal):
    metadata = {
        'food': ['Elephant', 'Jaguar', 'Penguin'],
        'new_animal': 1 / 75,
        'new_animal_energy': 15,
        'life_expectancy': 300,
        'food_frequency': [20, 40],
        'food_energy': 30
    }

    def __init__(self, time):
        super().__init__(time=time)


class Jaguar(Animal):
    metadata = {
        'food': ['Elephant', 'Tiger', 'Penguin'],
        'new_animal': 1 / 80,
        'new_animal_energy': 10,
        'life_expectancy': 350,
        'food_frequency': [35, 55],
        'food_energy': 20
    }

    def __init__(self, time):
        super().__init__(time=time)


class Elephant(Animal):
    metadata = {
        'food': ['Grass'],
        'new_animal': 1 / 200,
        'new_animal_energy': 7,
        'life_expectancy': 500,
        'food_frequency': [8, 15],
        'food_energy': 4
    }

    def __init__(self, time):
        super().__init__(time=time)


class Penguin(Animal):
    metadata = {
        'food': ['Cephalopod'],
        'new_animal': 1 / 80,
        'new_animal_energy': 10,
        'life_expectancy': 90,
        'food_frequency': [4, 15],
        'food_energy': 5
    }

    def __init__(self, time):
        super().__init__(time=time)


class Cephalopod:
    ident = ''

    def die(self, reason, time):
        pass


class Grass:
    ident = ''

    def die(self, reason, time):
        pass
