# Program that can find the minimum index of two lists

L1 = ['pizza', 'nuggets', 'hotdog', 'noodles', 'pasta', 'burger']

L2 = ['burger', 'hotdog', 'noodles', 'pasta', 'nuggets', 'pizza']

index_1 = 10
index_2 = 10

for i in range(len(L1)):
    index = L2.index(L1[i])

    if i + index < index_1 + index_2:
        index_1 = i
        index_2 = index

print(L1[index_1], index_1 + index_2)
