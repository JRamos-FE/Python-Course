# Program that can find the maximum numbers from a given set

numbers = int(input('Enter the amount of numbers you want to find the max of: '))

count = 0
maximum = 0

while count < numbers:
    n = int(input('Enter a number: '))
    if n >= maximum:
        maximum = n
        count += 1
    else:
        count += 1
print('Max = ', maximum)
