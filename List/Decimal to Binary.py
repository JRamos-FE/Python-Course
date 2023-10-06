# Program that can convert decimal to binary

n = int(input('Enter a number: '))

binary = ''

while n > 0:
    remainder = n % 2
    n //= 2
    binary += str(remainder)

print(binary)

