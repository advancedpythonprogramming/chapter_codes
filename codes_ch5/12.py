# 12.py


class Operations:

    @staticmethod
    def divide(num, den):
        # Check if the input parameters are a valid type
        if not (isinstance(num, int) and isinstance(den, int)):
            raise TypeError('Invalid input type.')

        # Check the numerator and denominator are greater than 0
        if num < 0 or den < 0:
            # The message inside brackets will show once the
            # exception has been handled.
            raise Exception('Negative values. Check the input parameters')

        return float(num) / float(den)


# In this code section we manage the runtime exception using try and except
# sentences.

# First example, using float values
try:
    print('First case: {}'.format(Operations().divide(4.5, 3)))

except (ZeroDivisionError, TypeError) as err:
    # This block works with the already defined exception types
    print('Error: {}'.format(err))

except Exception as err:
    # This block only handles type Exception exceptions
    print('Error: {}'.format(err))


# Second example, using negative values
try:
    print('Second case: {}'.format(Operations().divide(-5, 3)))

except (ZeroDivisionError, TypeError) as err:
    # This block works with the already defined exception types
    print('Error: {}'.format(err))

except Exception as err:
    # This block only handles type Exception exceptions
    print('Error: {}'.format(err))
