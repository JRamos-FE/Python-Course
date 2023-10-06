#Program that can sum the total of the integers for a number

n = int(input('Enter a number: '))

sum = 0

while n > 0:
    r = n % 10
    n //= 10
    sum += r

print('Sum = ', sum)