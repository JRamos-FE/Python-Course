# Program to find the AP series

a = int(input('Enter a number for the starting term: '))
d = int(input('Enter a number for the difference term: '))
n = int(input('Enter the amount of terms to be printed: '))

for i in range(a, a + n * d, d):
    print(i)


