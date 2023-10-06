# Program that can add the sum of given numbers

numbers = int(input('Enter the amount of numbers you want to add: '))

count = 0
total = 0

while count < numbers:
    n = int(input('Enter a number: '))
    total += n
    count += 1

print('Sum = ', total)
