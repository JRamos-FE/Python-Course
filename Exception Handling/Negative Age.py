# Program that will print the categorization of someones age based on a number
# Will return with a function, and includes exeption handling

user_age = int(input('Enter your age: '))


# Creating the function
def stage(age):
    if age < 0:
        raise NegativeAgeException('Age should not be negative.')
    elif age < 13:
        print('Kid')
    elif 13 <= age <= 19:
        print('Teen')
    elif 19 < age <= 50:
        print('Young')
    else:
        print('Old')


# Creating the exception class
class NegativeAgeException(Exception):
    pass


# Calling the function inside try and except
try:
    stage(user_age)
except NegativeAgeException as e:
    print(e)
