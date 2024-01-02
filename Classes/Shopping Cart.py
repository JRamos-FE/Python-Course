# Program related to overriding dealing with shopping

# Orders class
class Orders:
    def __init__(self):
        self.cart = []

    def add_to_cart(self, item):
        self.cart.append(item)
    
    def remove(self, item):
        self.cart.remove(item)

    def __len__(self):
        length = len(self.cart)
        return length
    
    def __str__(self):
        items = 'Cart Contents: '
        for i in self.cart:
            items += i + ', '
        return items
    
# Calling and creating object
o1 = Orders()
o1.add_to_cart('Tomato')
o1.add_to_cart('Rice')
o1.add_to_cart('Cake')

print('Cart Size: ', len(o1))
print(o1)