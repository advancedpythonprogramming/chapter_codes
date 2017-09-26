a_list = ["a", "b", "c", "d"]

for i, j in enumerate(a_list):
    print("{}: {}".format(i, j))

print([pair for pair in enumerate(a_list)])

# We create a dictionary using the index given by "enumerate" as key
print({i: j for i, j in enumerate(a_list)})
