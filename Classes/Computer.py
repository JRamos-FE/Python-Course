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
            self.name = name
        
        def get_name(self):
            return self.name
        
    def __init__(self, name, cpu, os):
        self.name = name
        self.CPU = cpu
        self.OS = os
    
    def __str__(self):
        return f'Name: {self.name}\n CPU: {self.CPU.get_make()}\n OS {self.OS.get_name()}'
        
# Creating and calling an object
cpu1 = Computer.CPU('Intel')
os1 = Computer.OS('Linux')
com1 = Computer('X1', cpu1, os1)
print(com1)