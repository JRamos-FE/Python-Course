# Program to check whether a string is a palindrome

sstring = input('Enter a string: ')

rev = sstring[::-1]

if sstring == rev:
    print('Palindrome')
else:
    print('Not a palindrome')