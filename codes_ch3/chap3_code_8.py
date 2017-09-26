variables = ['name', 'lastname', 'email']
p1 = ["John", 'Smith', 'js1@hotmail.com']
p2 = ["Thomas", 'White', 'thwh@gmail.com']
p3 = ["Jeff", 'West', 'jwest@yahoo.com']

contacts = []
for p in p1,p2,p3:
    contact = zip(variables, p)
    contacts.append(dict(contact))

for c in contacts:
    print("Name: {name} {lastname}, email: {email}".format(**c))
    #**c passes the dictionary as a keyworded list of arguments
