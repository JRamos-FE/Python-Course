# Program to find the Fibonacci sequence

n = int(input('Enter amount of terms: '))

a = 0
b = 1

for i in range(n):
    print(a)
    c = a + b
    a = b
    b = c