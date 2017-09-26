# 17.py


class Operations:

    @staticmethod
    def divide(num, den):
        if not (isinstance(num, int) and isinstance(den, int)):
            raise TypeError('Invalid input type')

        if num < 0 or den < 0:
            raise Exception('Negative input values')

        return float(num) / float(den)


# Open a text file in write mode
fid = open('log.txt', 'w')

try:
    # Check if we canwrite a line with the output of each operation.
    # This will yield an error beacuse 0 denominator

    [fid.write('{}'.format(
        Operations().divide(10, i))) for i in range(5, -1, -1)]

except (ZeroDivisionError, TypeError):
    # This block handle errors Este bloque opera para los tipos de excepciones
    # definidos
    print('Error!: Check the input parameters!')

else:
    print('No errors!')

finally:
    # This block assure that the file be closed correctely, even with a runtime
    # error
    print('Remember ALWAYS to close your files\n')
    fid.close()
