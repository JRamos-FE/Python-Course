# Program that can check if the max difference between two numbers is 5

# Taking user input as variables
num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))


# Function creation for difference
def diff(x, y):
    result = abs(x - y)
    # If-else statement to verify if result is less than or equal to 5
    if result <= 5:
        print('True, difference = ', result)
    else:
        print('False, difference = ', result)


# Calling the function
diff(num1, num2)
