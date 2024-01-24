# Project that determines whether a phrase is a pangram

# User input phrase
user_phrase = input('Enter a phrase: ')


# Creating function
def pangram(phrase):
    # Converting to lowercase
    lower_phrase = phrase.lower()

    # Creating a set for phrase
    phrase_set = set(lower_phrase)

    # Creating a dictionary that includes all the letters in English
    alphabet = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z', ' ', ',', '.'}

    for letter in phrase_set:
        if letter not in alphabet:
            print('The phrase is not an anagram.')
            break
    else:
        print('The phrase is a anagram')


# Calling the function
pangram(user_phrase)
