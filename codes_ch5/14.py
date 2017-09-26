# 14.py


class Operations:

    @staticmethod
    def divide(num, den):
        if not (isinstance(num, int) and isinstance(den, int)):
            raise TypeError('Invalid input type')

        if num < 0 or den < 0:
            raise Exception('Negative input values')

        return float(num) / float(den)


# In this section we handle the excetions
try:
    print(Operations().divide(4, 0))

except Exception as err:
    # This block works for all exception types.
    print('Error: {}'.format(err))
    print('Check the input')
