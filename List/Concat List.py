# Program that can concactenate a list into a single number

L1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

S1 = ''

for x in L1:
    S1 += str(x)

print(int(S1))
