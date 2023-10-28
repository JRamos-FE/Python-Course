# Program that can call a function to find the minimum numeric values

# Creating the function
def minimum(*vals, low_limit = None):
    # If there is no lower limit, return minimum operation for argument values
    if low_limit is None:
        return min(vals)
    # If there is a lower limit, take a new list of arguments that are equal or greater than the limit and then return the minimum of the list values
    else:
        L = [x for x in vals if x >= low_limit]
        return min(L)

# Calling the function
lower_limit = minimum(6, 7, 5, -9, low_limit = 4)
print('The lower limit of the arguments is = ', lower_limit)
