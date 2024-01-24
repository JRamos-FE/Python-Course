import array

ar1 = array.array('i', [10, 20, 30, 40])
print(ar1)

s1 = b'abcdef'
ar2 = array.array('b', s1)
print(ar2)

print(ar2[0])
print(ar2[1:3])
ar2.append(103)
print(ar2)
print(ar2.index(102))
