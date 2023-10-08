# Program that can take and find the max of three numbers

# Taking user input for variables
num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))
num3 = int(input('Enter the third number: '))

# Creating function max3 to find the greatest among the three
def max3(x, y, z):
    if x > y and x > z:
        print('Maximum = ', x)
    elif y > x and y > z:
        print('Maximum = ', y)
    elif z > x and z > y:
        print('Maximum = ', z)
    elif x == y == z:
        print('All are eqaul')
    else:
        print('Invalid')

# Calling the function
max3(num1 ,num2, num3)
