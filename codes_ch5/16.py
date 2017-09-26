# 16.py

class TransactionError(Exception):
    def __init__(self, funds, expenses):
        super().__init__("The money on your wallet is not enough to pay ${}"
                         .format(expenses))
        self.funds = funds
        self.expenses = expenses

    def excess(self):
        return self.funds - self.expenses


class Wallet:
    def __init__(self, money):
        self.funds = money

    def pay(self, expenses):
        if self.funds - expenses < 0:
            raise TransactionError(self.funds, expenses)
        self.funds -= expenses

if __name__ == '__main__':
    b = Wallet(1000)

    try:
        b.pay(1500)
    except TransactionError as err:
        print('Error: {}'.format(err))
        print("There is an excess of expenses of ${}".format(err.excess()))
