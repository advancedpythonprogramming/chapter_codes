# Lets suppose we want to decorate a class such that it prints a warning
# when we try to spend more than what we've got
def add_warning(cls):
    prev_spend = getattr(cls, 'spend')

    def new_spend(self, money):
        if money > self.money:
            print("You are spending more than what you have, "
                  "a debt has been generated in your account!!")
        prev_spend(self, money)

    setattr(cls, 'spend', new_spend)
    return cls


@add_warning
class Buy:
    def __init__(self, money):
        self.money = money
        self.debt = 0

    def spend(self, money):
        self.money -= money
        if self.money < 0:
            self.debt = abs(self.money)  # the debt is considered positive
            self.money = 0
        print("Current Balance = {}".format(self.money))


b = Buy(1000)
b.spend(1200)