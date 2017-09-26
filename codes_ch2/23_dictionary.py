dogs = {'bc': 'border-collie', 'lr': 'labrador retriever', 'pg': 'pug'}
telephones = {23545344: 'John', 23545340: 'Trinity', 23545342: 'Taylor'}
tuples = {('23545344', 0): 'office', ('2353445340', 1): 'admin'}

print(dogs)
print(tuples)

# We access directly to the value using its key
print(dogs['bc'])
print(telephones[23545344])

# If a key does not exist, Python creates a new one and assigns the value
dogs['te'] = 'terrier'
print(dogs)

# If the key already exist, Python just assigns the value
dogs['pg'] = 'pug-pug'
print(dogs)

# We remove items using del
del dogs['te']
print(dogs)

# The sentence in checks whether exist a specific key in the dictionary
print('pg' in dogs)
print('te' in dogs)

# The method get() checks whether a key exists or not.

print(dogs.get('pg', False))  # logical value as default
print(dogs.get('te', 2))  # int value as default
print(dogs.get('te', 'The dog does not exist'))  # String value as default
