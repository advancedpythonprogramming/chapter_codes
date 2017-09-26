from collections import deque
from package import Package
from bottle import Bottle


class Machine:

    def process(self, incoming_production_line):
        print("----------------------")
        print("Machine {} started working.".format(
            self.__class__.__name__))


class BottleModulator(Machine):

    def __init__(self):
        self.bottles_to_produce = 0

    def process(self, incoming_production_line=None):
        super().process(incoming_production_line)
        # --------------
        # Complete the method
        # --------------
        return None


class LowFAT32(Machine):

    def __init__(self):
        self.discarded_bottles = []

    def discard_bottle(self, bottle):
        self.discarded_bottles.append(bottle)

    def print_discarded_bottles(self):
        print("{} bottles were discarded".format(
            len(self.discarded_bottles)))

    def process(self, incoming_production_line):
        # -----------------
        # Complete the method
        # -----------------
        return None


class HashSoda9001(Machine):

    def process(self, incoming_production_line):
        super().process(incoming_production_line)
        # ----------------
        # Complete the method
        # ----------------
        return None


class PackageManager(Machine):

    def process(self, incoming_production_line):
        packages = deque()
        for stack in incoming_production_line.values():
            package = Package()
            package.add_bottles(stack)
            packages.append(package)
        return packages


class Factory:

    def __init__(self):
        self.bottlemodulator = BottleModulator()
        self.lowFAT32 = LowFAT32()
        self.hashSoda9001 = HashSoda9001()
        self.packageManager = PackageManager()

    def producir(self, num_bottles):
        self.bottlemodulator.bottles_to_produce = num_bottles
        product = None
        for machine in [self.bottlemodulator,
                        self.lowFAT32,
                        self.hashSoda9001,
                        self.packageManager]:
            product = machine.process(product)
        return product


if __name__ == "__main__":

    num_bottles = 423

    factory = Factory()
    output = factory.producir(num_bottles)
    print("----------------------")
    print("{} bottles produced {} packages".format(
        num_bottles, len(output)))
    for package in output:
        package.see_content()
    print("----------------------")
