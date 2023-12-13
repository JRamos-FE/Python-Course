# Program related to accessors mutators
# Using a class for customers, access and set the customer info

# Customer class
class Customer:
    def __init__(self, name, phonenum):
        self.name = name
        self.phonenum = phonenum

    def get_name(self):
        cust_name = self.name
        return cust_name
    
    def get_phonenum(self):
        cust_num = self.phonenum
        return cust_num
    
    def set_phonenum(self, new_phonenum):
        self.phonenum = new_phonenum
        return new_phonenum
    
# Creating a customer
cust1 = Customer('Joseph', 8129460934)

# Calling the methods
print(cust1.get_name())
print(cust1.get_phonenum())

# Creating a new phone number for this customer
print(cust1.set_phonenum(8122073509))
