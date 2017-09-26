# 27.py

import string
import random


class StringUpper(list):

    def __enter__(self):
        return self

    def __exit__(self, type, value, tb):
        for i in range(len(self)):
            self[i] = self[i].upper()


with StringUpper() as s_upper:
    for i in range(20):
        # Here we randomly select a lower case ascii
        s_upper.append(random.choice(string.ascii_lowercase))
    print(s_upper)

print(s_upper)
