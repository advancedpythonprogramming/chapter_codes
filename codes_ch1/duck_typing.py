# duck_typing.py


class Duck:

    def scream(self):
        print("Cuack!")

    def walk(self):
        print("Walking like a duck...")


class Person:

    def scream(self):
        print("Ahhh!")

    def walk(self):
        print("Walking like a human...")


def activate(duck):
    duck.scream()
    duck.walk()

if __name__ == "__main__":
    Donald = Duck()
    John = Person()
    activate(Donald)
    # this is not supported in other languajes, because John
    # is not a Duck object
    activate(John)
