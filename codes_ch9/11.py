# 11.py

items_bought = [('milk', 2, 120), ('bread', 3.5, 800), ('rice', 1.75, 960)]

print("PRODUCT  QUANTITY   PRICE   SUBTOTAL")
for product, price, quantity, in items_bought:
    subtotal = price * quantity
    print("{0:8s}{1: ^9d}    ${2: <8.2f}${3: >7.2f}"
          .format(product, quantity, price, subtotal))
