currency = {'Chile': 'Peso', 'Brazil': 'Real',
           'Peru': 'Sol', 'Spain': 'Euro', 'Italy': 'Euro'}

print(currency.keys())  # returns a list with the keys
print(currency.values())  # returns a list with the values
print(currency.items())  # returns a list of tuples key-value

# Iteration over a dictionary

# By default Python iterates directly over the keys
print('This dictionary has the following keys:')

for k in currency:
    print('{0}'.format(k))

# Although we can also use the method keys()
print('This dictionary has the following keys:')

for k in currency.keys():
    print('{0}'.format(k))

# We use the method values() when we want to iterates using the values
print('The values in the dictionary:')
for v in currency.values():
    print('{0}'.format(v))

# The method items() allows us to retrieve a tuple (key, value)
print('The pairs key-value:')

for k, v in currency.items():
    print('the currency in {0} is {1}'.format(k, cv))