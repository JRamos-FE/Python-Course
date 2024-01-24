import copy

# List
L = [10, 20, 30, 40, 50]

# Shallow copy
L1 = copy.copy(L)
print(L1)
x = id(L)
print(x)
y = id(L1)
print(y)
x0 = id(L[0])
print(x0)
y0 = id(L1[0])
print(y0)


# Deep copy
class Person:
    def __init__(self, name):
        self.name = name


Lp = [Person('James'), Person('Timothy'), Person('Jim')]
L2 = copy.deepcopy(L)
x2_0 = id(Lp[0])
print(x2_0)
y2_0 = id(L2[0])
print(y2_0)