# Program for a customer bank account using a class

# Custom exception class
class MinimumBalanceError(Exception):
    def __init__(self, message="Account balance is below minimum allowed"):
        self.message = message
        super().__init__(self.message)


# Bank account class
class Account:
    AccNumber = 1001

    def __init__(self, name, balance=1000):
        if balance < 1000:
            raise MinimumBalanceError('Account Creation Error - Initial balance is below minimum allowed')
        self.name = name
        self.balance = balance
        self.account_number = Account.AccNumber
        Account.AccNumber += 1

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount < 1000:
            raise MinimumBalanceError('Withdrawal Error - Account balance would fall below the minimum allowed')
        self.balance -= amount

    def show_details(self):
        print(f'Account Number: {self.account_number}')
        print(f'Name: {self.name}')
        print(f'Balance: {self.balance}')


# Example usage
try:
    ac1 = Account('Jose', 200)
except MinimumBalanceError as e:
    print(f"Error: {e}")

ac2 = Account('James', 3000)
ac2.show_details()
