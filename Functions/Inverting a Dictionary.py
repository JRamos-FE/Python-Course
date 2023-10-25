# Program to invert a dictionary, keys to values and values to keys

# Dictionaries and contents
before = {'a': 10, 'b': 20, 'c': 30, 'd': 40}


def invert_dict(x):
    # Taking values/keys and assigning values
    keys_1 = list(x.keys())
    values_1 = list(x.values())
    keys_after = values_1
    values_after = keys_1

    # Creating the new inverted dictionary
    after = dict(zip(keys_after, values_after))

    # Returning the new dictionary
    return after

# Calling and printing the function
idict = invert_dict(before)
print(idict)

