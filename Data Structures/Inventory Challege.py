# Program related to inventory management
# A dictionary where the items (fruit) are keys and values (amount)

from collections import Counter

# Initial inventory
inventory = Counter({'apple': 50, 'mango': 100, 'banana': 120, 'orange': 70})


def update_inventory(customer_amount):
    inventory.subtract(customer_amount)


order = Counter(apple=10, banana=12, orange=5)
update_inventory(order)

print(inventory)