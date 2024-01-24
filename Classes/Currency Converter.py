# Program that can convert currencies from one to another

# Currency class
class CurrencyConvertor:
    def __init__(self, currency, rate):
        self.amount = None
        self.currency = currency
        self.rate = rate

    def set_currency(self, new_currency):
        self.currency = new_currency
        return f'Currency: {self.currency}'

    def get_currency(self):
        return f'Currency: {self.currency}'

    def set_rate(self, new_rate):
        self.rate = new_rate
        return f'Rate: {self.rate}'

    def get_rate(self):
        return f'Rate: {self.rate}'

    def convert(self, amount):
        self.amount = amount
        return f'Amount: {self.rate * self.currency}'


# Creating class object
con1 = CurrencyConvertor('USD', 20)

# Calling the methods and printing
print(con1.get_currency())
print(con1.get_rate())

# Mutator methods
print(con1.set_currency('AUD'))
print(con1.set_rate(.66))
