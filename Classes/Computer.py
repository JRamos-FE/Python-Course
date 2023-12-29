# Program for a class dealing with computers and its components

# Computer class
class Computer:
    # CPU Class
    class CPU:
        def __init__(self, make):
            self.make = make
            
        def get_make(self):
            return self.make

    # Operating System Class    
    class OS:
        def __init__(self, name):
            return self.name
        
        def get_name(self):
            return self.name
        
    def __init__(self, name, CPU, OS):
        self.name = name
        self.CPU = CPU
        self.OS = OS
    
    def __str__(self):
        return f'Name: {self.name}\n CPU: {self.CPU}\n OS: {self.OS}'
        
# Creating and calling an object
cpu1 = CPU('Intel')
os1 = OS('Linux')
com1 = Computer('X1', cpu1, os1)
print(com1)