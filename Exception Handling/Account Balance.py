# Program to check the current account balance

# User input to withdraw
user_withdraw = int(input('Enter an amount to withdraw: '))

balance = 10000
min_balance = 5000

# Function to withdraw creation
def withdraw(amount):
    global balance # Access to global variable
    if balance - amount < min_balance:
        raise AccountBalanceException('Balance should not be less than $5,000')
    balance -= amount
    return balance

# Creating the exception class
class AccountBalanceException(Exception):
    pass

# Calling the function from within the try exept
try:
    new_balance = withdraw(user_withdraw)
    print('Withdrawl successful \n Current balance = ', new_balance)
except AccountBalanceException as a:
    print(a)
