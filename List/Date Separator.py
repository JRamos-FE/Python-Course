# Program that can find the day, month, and year from given date

date = input('Enter a date (dd/mm/yy): ')

split = date.split('/')

print('Day: ', split[0])
print('Month: ', split[1])
print('Year: ', split[2])

