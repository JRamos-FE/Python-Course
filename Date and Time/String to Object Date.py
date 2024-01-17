# Program that deals with converting a string into a date object

# Importing modules
import datetime

# User input
str_date = input('Enter the date (day, month, year): ')

# Splitting the input
day, month, year = str_date.split(',')

# Clearing white space
day = day.strip()
month = month.strip()
year = year.strip()

# Converting to integer
day = int(day)
month = int(month)
year = int(year)

# Converting to date object
d1 = datetime.date(year, month, day)

print('Date: ', d1)
