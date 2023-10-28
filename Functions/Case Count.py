# Project that can count the number of case specific letters are available for a phrase

# Taking user input
user_input = input('Enter a phrase: ')

# Creating a function
def count(phrase):
    # Variables
    upper_count = 0
    lower_count = 0
    other_count = 0
    # Iteration through the phrase
    for letter in phrase:
        if letter.isupper():
            upper_count += 1
        elif letter.islower():
            lower_count += 1
        else:
            other_count += 1
    print('Upper case = ', upper_count,'\n',
          'Lower Case = ', lower_count, '\n',
          'Other = ', other_count)
    
# Calling the function
count(user_input)