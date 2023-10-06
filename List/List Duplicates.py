# Program that removes duplicates from a given list

list1 = [1,1,2,3,4,54,6,7,8,3,2,1,4,5,7,7,8]
l2 = []

for x in list1:
    if x not in l2:
        l2.append(x)

print('The unique elements from the list are: ', l2)