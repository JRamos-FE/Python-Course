# Program that deals with counter objects to return a bill

from collections import Counter

# Price of items
price = Counter({'Soap': 2, 'Toothpaste': 5, 'Shampoo': 8, 'Toothbrush': 10})

# Amount of items
cart = Counter(Soap=5, Toothpaste=1, Shampoo=2, Toothbrush=3)


def update_inventory(items_price, items_quantity):
    result = Counter()
    for item in items_price:
        if item in items_quantity:
            result[item] = items_price[item] * items_quantity[item]
    return result


pricing = update_inventory(price, cart)

# Formatting the bill
bill_lines = ["Product\t Price\t Quantity\t Total"]
for x in pricing:
    line = f"{x}:\t ${price[x]}\t x{cart[x]}\t = ${pricing[x]}"
    bill_lines.append(line)
bill = '\n'.join(bill_lines)

print(bill)