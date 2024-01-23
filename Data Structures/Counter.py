from collections import Counter

L = ['Mark', 'Jonny', 'David', 'Mark', 'Jonny', 'Mark', 'James', 'Matthew']
c = Counter(L)
c.update({'Jose': 4})

for i in c.elements():
    print(i)
