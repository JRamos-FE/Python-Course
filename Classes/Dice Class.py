# Program that creates a class for Dice and its attributes

# Importing module
from random import randint


# Dice class
class Dice:
    def __init__(self, sides):
        self.sides = sides

    def roll_dice(self):
        return randint(1, self.sides)


d1 = Dice(89)
print(d1.roll_dice())
