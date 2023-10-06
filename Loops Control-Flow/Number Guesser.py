# Program that can guess a number between 1 through 10

import random

number = random.randint(1, 10)
guess = 0

while guess != number:
    guess = int(input('Guess a number between 1 and 10: '))
    if guess < number:
        print('Guess higher')
    elif guess > number:
        print('Guess lower')
    else:
        print('Correct')
