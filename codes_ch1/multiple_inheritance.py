# multiple_inheritance.py


class Researcher:

    def __init__(self, field):
        self.field = field

    def __str__(self):
        return "Research field: " + self.field + "\n"


class Teacher:

    def __init__(self, courses_list):
        self.courses_list = courses_list

    def __str__(self):
        out = "Courses: "
        for c in self.courses_list:
            out += c + ", "
        # the [:-2] selects all the elements
        # but the last two
        return out[:-2] + "\n"


class Professor(Teacher, Researcher):

    def __init__(self, name, field, courses_list):
        # This is not completetly right
        # Soon we will see why
        Researcher.__init__(self, field)
        Teacher.__init__(self, courses_list)
        self.name = name

    def __str__(self):
        out = Researcher.__str__(self)
        out += Teacher.__str__(self)
        out += "Name: " + self.name + "\n"
        return out


p = Professor("Steve Iams",
              "Meachine Learning",
              [
                "Python Programming",
                "Probabilistic Graphical Models",
                "Bayesian Inference"
              ])

print(p)
