# Program that counts the number of digits in an integer

# Take a number
n = int(input('Enter a number: '))

# initialize variable to count
counter = 0

# While the counter is less than
while n != 0:
    n //= 10
    counter += 1

print(counter)
