# Program that operates as password verification

pass1 = input('Enter a password: ')
pass2 = input('Enter a password: ')

if pass1 == pass2:
    print('Passwords match!')
else:
    if pass1.casefold() == pass2.casefold():
        print('Check for casing')
    else:
        print('Passwords do not match')
        