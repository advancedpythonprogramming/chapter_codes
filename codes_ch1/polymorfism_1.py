# polymorfism_1.py

class Variable:
    def __init__(self, data):
        self.data = data

    def representative(self):
        pass


class Income(Variable):
    def representative(self):
        return sum(self.data) / len(self.data)


class City(Variable):
    # class variable
    _city_pop_size = {'Shanghai': 24000, 'Sao Paulo': 21300, 'Paris': 10800,
                      'London': 8600, 'Istambul': 15000,
                      'Tokyo': 13500, 'Moscow': 12200}

    def representative(self):
        dict = {City._city_pop_size[c]: c for c in self.data
                if c in City._city_pop_size.keys()}
        return dict[max(dict.keys())]


class JobTitle(Variable):
    # class variable
    _range = {'CEO': 1, 'CTO': 2, 'Analyst': 3, 'Intern': 4}

    def representative(self):
        dict = {JobTitle._range[c]: c for c in self.data if
                c in JobTitle._range.keys()}
        return dict[min(dict.keys())]


if __name__ == "__main__":
    income_list = Income([50, 80, 90, 150, 45, 65, 78, 89, 59, 77, 90])
    city_list = City(['Shanghai', 'Sao Paulo', 'Paris', 'London',
                      'Istambul', 'Tokyo', 'Moscow'])
    job_title_list = JobTitle(['CTO', 'Analyst', 'CEO', 'Intern'])
    print(income_list.representative())
    print(city_list.representative())
    print(job_title_list.representative())
