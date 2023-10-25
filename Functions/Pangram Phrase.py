# Project that determines whether a phrase is a pangram

# User input phrase
phrase = input('Enter a phrase: ')

# Creating a dictionary that includes all the letters in English
letters = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}
# Creating function
def pangram(phrase):
    for letter in phrase:
        if letter
