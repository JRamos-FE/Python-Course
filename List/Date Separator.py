# Program that can find the day, month, and year from given date

date = input('Etner a date (dd/mm/yy): ')

splt = date.split('/')

print('Day: ', splt[0])
print('Month: ', splt[1])
print('Year: ', splt[2])

