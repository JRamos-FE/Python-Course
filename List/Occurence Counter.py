# Program that counts the number of occurences that an element appears in a list

L1 = ['A', 'B', 'C', 'D', 'E', 'A', 'B', 'E', 'B', 'D', 'B', 'E']
L_result = []


for x in L1:
    if x not in L_result:
        L_result.append(x)
        count = L1.count(x)
        L_result.append(count)

print(L_result)