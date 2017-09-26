# mro.py

from diamond_problem_solution import SubClassA

for c in SubClassA.__mro__:
    print(c)
