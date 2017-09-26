# 13.py


class Operations:

    @staticmethod
    def divide(num, den):
        if not (isinstance(num, int) and isinstance(den, int)):
            raise TypeError('Invalid input type')

        if num < 0 or den < 0:
            raise Exception('Negative input values')

        return float(num) / float(den)


# The complete Try/Except structure

try:
    # Check if we can excecute this operation
    resultado = Operations.divide(10, 0)

except (ZeroDivisionError, TypeError):
    # This block works with the already defined exception types
    print('Check the input values. '
          'They aren\'t ints or the denominator is 0')

except Exception:
    # This block only handles type Exception exceptions
    print('All given values are negative')

else:
    # When we do no have errors, the program excecute this lines
    print('Everything is ok. They were no errors')

finally:
    print('Rebember to ALWAYS use this structure to handle your runtime'
          'errors')
