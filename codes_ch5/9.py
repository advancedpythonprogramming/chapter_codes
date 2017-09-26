# 9.py


class Operations:

    @staticmethod
    def divide(num, den):
        if den == 0:
            # Here we generate the exception and we include
            # information about its meaning.
            raise ZeroDivisionError('Denominator is 0')
        return float(num) / float(den)


print(Operations().divide(3, 4))
print(Operations().divide(3, 0))
