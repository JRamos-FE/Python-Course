# Program that can find the sum of positive and negative numbers

numbers = int(input('Enter the amount of numbers you want to add: '))

count = 0
pos_total = 0
neg_total = 0

while count < numbers:
    n = int(input('Enter a number: '))
    if n < 0:
        neg_total += n
    else:
        pos_total += n
    count += 1

print('Positive Sum = ', pos_total, 'Negative Sum = ', neg_total)
