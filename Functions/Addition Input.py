# Program that can take in user input and add it through a function

# Function called addition
def addition(*args):
    total = 0
    for i in args:
        total += i
    return total

# User input
user_input = input('Enter the numbers to add: ')

# Utilizing split to seperate the numbers through a space
numbers = [int(x) for x in user_input.split()]

# Calling the function
result = addition(*numbers)

# Printing result
print(result)

