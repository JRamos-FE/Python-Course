# Program to check whether a number is a palindrome

n = int(input('Enter a numer: '))
rev = 0
m = n
while n > 0:
    r = n % 10
    n //= 10
    rev = rev * 10 + r

if rev == m:
    print('Palindrome')
else:
    print('Not a palindrome ', rev)