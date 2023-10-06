# Program to find the factorial of a number

n = int(input('Enter a number: '))

count = 1
fact = 1
for i in range(0,n):
    fact *= count
    count += 1
print(fact)