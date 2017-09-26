from Solucion.Bonus.animals import Tiger, Elephant, Penguin, Jaguar, Grass, Cephalopod

MAX_SIMUL_TIME = 100
MAX_NUM_OF_SIMULATIONS = 10.0


def run_simulation(time, animals, unlimited_food):
    while time < MAX_SIMUL_TIME and len(animals) != 0:
        time = min(animals.values())
        newborns = []
        deaths = []
        animals_with_actions = list(filter(lambda k: animals[k] == time, animals.keys()))

        for a in animals_with_actions:

            if a.moment_of_dead == time:  # they die
                a.die('old', time)

            if not a.dead and a.next_eating_time == time:  # they eat
                a.eat(list(filter(lambda k: not k.dead, animals.keys())) + unlimited_food, time)

            if not a.dead and a.next_new_animal_time == time:  # they born
                newborn = a.__class__(time)
                a.new_animal(time)
                newborns.append(newborn)

            if a.dead:
                deaths.append(a)
            else:
                animals.update({a: a.next_action_time()})

        if len(deaths) != 0:
            for dead in deaths:
                del animals[dead]

        if len(newborns) != 0:
            for nb in newborns:
                animals.update({nb: nb.next_action_time()})


def run(ecosystem, statistics):
    simul_time = []
    for i in range(int(MAX_NUM_OF_SIMULATIONS)):

        print(i)
        animals = {}
        time = 0
        unlimited_food = [Grass()] * ecosystem[Elephant] * 3 + [Cephalopod()] * ecosystem[Penguin] * 5
        for t, number in ecosystem.items():
            for _ in range(number):
                instance = t(time)
                animals.update({instance: instance.next_action_time()})
            t.statistics['current_num_animals'] = number

        simul_time.append(run_simulation(time, animals, unlimited_food))

        for t in ecosystem.keys():
            for stat_name, value in t.statistics.items():
                if stat_name != 'extinction_time':
                    statistics[t][stat_name] += value

                else:
                    if value != -1:
                        statistics[t][stat_name] += value
                        statistics[t]['extinction'] += 1

    return statistics, simul_time

if __name__ == "__main__":
    ecosystem = {
        Tiger: 10,
        Elephant: 10,
        Penguin: 10,
        Jaguar: 10
    }
    statistics = {_type: {'extinction': 0,
                          'extinction_time': 0,
                                'new_animal': 0,
                                'death_eaten': 0,
                                'death_no_energy': 0,
                                'death_old': 0,
                                'current_num_animals': 0,
                                'time_lived': 0,
                                'time_waited_for_food': 0,
                                'waited_for_food': 0
                          } for _type in ecosystem.keys()}
    # Starts
    statistics, simul_time = run(ecosystem, statistics)

    print("------------\nRESULTS\n------------")
    for _type, stats in statistics.items():
        print(_type.__name__.upper())
        print('Times extincted = {0}'.format(stats['extinction']))
        if stats['extinction'] > 0:
            print('Average time of specie survival when extincted = {0}'.format(stats['extinction_time']/stats['extinction']))
        print('Average number of newborns = {0}'.format(stats['new_animal'] / MAX_NUM_OF_SIMULATIONS))
        print('Average number of {0} eaten by other animals = {1}'.format(_type.__name__,
                                                                          stats['death_eaten'] / MAX_NUM_OF_SIMULATIONS))
        print(
            'Average number of deaths caused by lack of energy = {0}'.format(stats['death_no_energy'] / MAX_NUM_OF_SIMULATIONS))
        print('Average number of deaths caused by aging = {0}'.format(stats['death_old'] / MAX_NUM_OF_SIMULATIONS))

        if stats['death_eaten'] + stats['death_no_energy'] + stats['death_old'] > 0:
            print('Average age of death = {0}'.format(stats['time_lived'] /
                                                      (stats['death_eaten'] +
                                                       stats['death_no_energy'] +
                                                       stats['death_old'])))
        print('Average number of {0} by the end of simulation time = {1}'.format(_type.__name__,
                                                                                 stats[
                                                                                     'current_num_animals'] / MAX_NUM_OF_SIMULATIONS))
        print('Average number of {0} that waited for food = {1}'.format(_type.__name__,
                                                                        stats['waited_for_food'] / MAX_NUM_OF_SIMULATIONS))
        if stats['waited_for_food'] != 0:
            print('Average time waited for food = {0}'.format(stats['time_waited_for_food'] / stats['waited_for_food']))
