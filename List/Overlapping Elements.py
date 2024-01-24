# Program that can find the overlapping elements in both lists given

L1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

L2 = [1, 2, 3, 4, 5, 6, 11, 22, 33, 44]

L3 = []

for x in L1:
    if x in L2:
        L3.append(x)

print(L3)
