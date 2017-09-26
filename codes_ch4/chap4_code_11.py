def see_weight(self):
    print(self.weight)

MyBody = type("MyBody", (Body,), {"see_weight": see_weight})
print(hasattr(Body, "see_weight"))
print(hasattr(MyBody, "see_weight"))
print(getattr(MyBody, "see_weight"))
print(getattr(MyBody(), "see_weight"))

m1 = MyBody()
m1.see_weight()
