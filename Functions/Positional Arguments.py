# Program that has a function take two positional arguments, as strings and concatenates them

# Taking suer input
str1 = input('Enter your name: ')
str2 = input('Enter your profession: ')


# Creating the function
def message(string1, string2):
    print(f'Hello my name is {string1}, I am a {string2}')


# Calling the function
message(str1, str2)
