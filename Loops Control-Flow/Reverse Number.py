# Program that gives the digits in reverse of a number

n = int(input('Enter a number: '))
rev = 0

while n > 0:
    r = n % 10
    n //= 10
    rev = rev * 10 + r

print(rev)
