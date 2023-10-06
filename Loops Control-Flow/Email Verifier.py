# Program that can find the user id and domain from an email address

email = input('Enter your email: ')

atrate = email.find('@')

print('User ID = ', email[:atrate])
print('Domain Name = ', email[atrate + 1:])
