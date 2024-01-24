# Program related to overriding of class methods

# Robot class
class Robot:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        return 'Hello, how can I help you?'


class PoliceRobot(Robot):
    def say_hi(self):
        return 'Police Robot, how can I help you?'


# Creating and calling objects
rb1 = Robot('X24')
prb1 = PoliceRobot('PCX24')

print(rb1.say_hi())
print(prb1.say_hi())
