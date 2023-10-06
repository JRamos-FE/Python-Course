# Program that checks and removes if there are any duplicates in a list

L1 = [3,4,5,6,4,3,4,5,2,3,4,5,6,7,8,6,5,4,3]
L2 = []

for x in L1:
    if x not in L2:
        L2.append(x)

print(L2)