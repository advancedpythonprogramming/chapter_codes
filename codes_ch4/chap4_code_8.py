# a function that will be used as a method in the class we shall create
def lose_weight(self, x):
    self.weight -= x

Body = type("Body", (), {"weight": 100, "lose_weight": lose_weight})
bd = Body()

print(bd.weight)
bd.lose_weight(10)
print(bd.weight)
