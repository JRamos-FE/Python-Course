# Program that takes the first 10 variables of an integer
n = int(input('Enter an integer: '))


counter = 0

while counter <= 10:
    print(n, ' x ', counter, ' = ', n * counter)
    counter += 1