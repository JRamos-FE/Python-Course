# Program to flatten a nested sequence using a function

# Nested list
items = [1000, 221, [-3, 344, [25, 426], 3247], 4358]

# Creating function
def flatten(seq):
    for element in seq:
        # Object has the attribute iteration
        if hasattr(element, '__iter__'):
            yield from flatten(element) #Recursive call of yield for objects within the nested list
        # Object is any other type
        else:
            yield element

# Calling the function
x = list(flatten(items))
print(x)