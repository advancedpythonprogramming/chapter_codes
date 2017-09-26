# 11.py


class Operations:

    @staticmethod
    def divide(num, den):
        # This method will raise an exception when denominator be 0
        return float(num) / float(den)


try:
    # Here we manage the exceptions during the runtime of the function.
    # The first case will return an output and the second case will yield and
    # error beacuse denominator is 0. The output in this wont be printed.

    print('First case: {}'.format(Operations().divide(4, 5)))
    print('Second case: {}'.format(Operations().divide(4, 0)))

except ZeroDivisionError as err:
    print('Error: {}'.format(err))
