# Notes on datatypes used in Numpy

import numpy as np

# b = byte
# B - unsigned byte
# i - integer
# u - Unsigned Integer
# f - Float
# F - Complex Float
# m - timedelta
# M - datetime
# O - Object
# S - string
# U - Unicode String
# ? - boolean

ar1 = np.array([1, 2, 3, 4], 'b')  # Array with 1 byte element size, range -128-127
print(ar1.dtype)

ar1 = np.array([1, 2, 3, 4], 'B')  # Array with 1 byte element size, range 0-255
print(ar1.dtype)

ar1 = np.array([1, 2, 3, 4], 'i')
print(ar1.dtype)


ar1 = np.array([1, 2, 3, 4], 'f')
print(ar1.dtype)

ar1 = np.array([1, 2, 3, 4], 'm')
print(ar1.dtype)


ar1 = np.array([1, 2, 3, 4], 'O')
print(ar1.dtype)

ar1 = np.array([1, 2, 3, 4], 'S')
print(ar1.dtype)

ar1 = np.array(['a', 'b', 'c', 'd'], 'U')
print(ar1.dtype)

ar1 = np.array([1, 2, 3, 4], '?')
print(ar1.dtype)