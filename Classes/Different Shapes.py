from abc import ABC, abstractmethod
from math import pi


# Shape class
class Shape(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def area(self):
        pass


# Rectangle subclass
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__("Rectangle")
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


# Circle subclass
class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2


# Creating and calling objects
# Note: We cannot instantiate Shape as it's an abstract class
rect = Rectangle(4, 5)
circle = Circle(4)

print(f'Area of {rect.name}: {rect.area()}')
print(f'Area of {circle.name}: {circle.area()}')
