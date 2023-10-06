# Program that can display data of a particular item for name and price

name = input('Enter a product name: ')
price = input('Enter a product price: ')

tot_len = len(name) + len(price)

dots = '.' * (25 - tot_len)

print(name + dots + price)
