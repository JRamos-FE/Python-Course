# Program that will utilize inheritance to call subclasses for shapes

# Polygon class
class Polygon:
    def __init__(self, num_sides, *side_dimensions):
        self.num_sides = num_sides
        self.side_dimensions = side_dimensions

    def describe(self):
        print(f'This shape has {self.num_sides} sides with the following dimensions: {self.side_dimensions}')

# Triangle class
class Triangle(Polygon):
    def __init__(self,area):
        self.area = area

# Creating a shape
poly1 = Polygon(5, 2, 4, 5, 6, 8)
poly1.describe()