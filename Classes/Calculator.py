# Program that functions as a calculator using a class

# Claculator class
class Calculator:
    # Default values
    default_num1 = 0
    default_num2 = 0

    def __init__(self, num1 = default_num1, num2 = default_num2):
        self.num1 = num1
        self.num2 = num2
    
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def sub(a, b):
        return a - b
    
    @staticmethod
    def mul(a, b):
        return a * b
    
    @staticmethod
    def div(a, b):
        return a // b
    
# Contstructing a calculator class object
cal1 = Calculator(22, 33)

# Calling a method
print(cal1.add())
