# 15.py


class Exception1(Exception):
    pass


class Exception2(Exception):

    def __init__(self, a, b):
        super().__init__("One of the values {0} or {1} is not integer"
                         .format(a, b))


class Operations:

    @staticmethod
    def divide(num, den):
        # In this example, we re-define exceptions that we used in the last
        # examples.

        if not (isinstance(num, int) and isinstance(den, int)):
            raise Exception2(num, den)

        if num < 0 or den < 0:
            raise Exception1('Negative values\n')

        return float(num) / float(den)


# This case raise the exception 1
try:
    print(Operations().divide(4, -3))

except Exception1 as err:
    # This block works for type one exception
    print('Error: {}'.format(err))

except Excepcion2 as err:
    # This block works for type two exception
    print('Error: {}'.format(err))


# This case raise the exception 2
try:
    print(Operations().divide(4.4, -3))

except Exception1 as err:
    # This block works for type one exception
    print('Error: {}'.format(err))

except Exception2 as err:
    # This block works for type two exception
    print('Error: {}'.format(err))
