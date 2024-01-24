# Program for circle class

# Importing math library
import math


# Circle class
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        area = math.pi * (self.radius ** 2)
        return area

    def perimeter(self):
        perimeter = 2 * math.pi * self.radius
        return perimeter


c1 = Circle(33)
print(f'{c1.area():.3f}')
print(f'{c1.perimeter():.3f}')
