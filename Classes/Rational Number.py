# Program related to operator overloading and rational numbers

# Rational class
class Rational:
    def __init__(self, p, q):
        self.p = p
        self.q = q

    def __add__(self, other):
        p = self.p * other.q + self.q * other.p
        q = self.q * other.q
        sum = Rational(p, q)
        return sum

    def __sub__(self, other):
        p = self.p * other.q - self.q * other.p
        q = self.q * other.q
        deduc = Rational(p, q)
        return deduc

    def __str__(self):
        return f'Rational Number = {self.p} / {self.q}'


# Creating and calling an object
r1 = Rational(4, 6)
r2 = Rational(1, 2)

r3 = r1 + r2
print(r3)
