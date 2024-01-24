# Program dealing with operator overloading and angle class

# Angle class
class Angle:
    def __init__(self, degree):
        self.degree = degree

    def __add__(self, ang):
        sum = Angle(self.degree + ang.degree)
        return sum

    def __str__(self):
        return f'Degree: ' + str(self.degree)


# Calling an object
ang1 = Angle(32)
ang2 = Angle(44)
ang3 = ang1.__add__(ang2)
print(ang3)
