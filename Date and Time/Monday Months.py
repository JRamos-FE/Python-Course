# Program that deals with date and time functions
# Returns the amount of months that begin on a Monday for a given year

# Importing modules
import datetime

# User Input: Year
year = int(input('Enter the desired year: '))
# Date object for given year
monday = 0

# Loop through iteration of months
for month in range(1, 13):
    dt = datetime.date(year, month, 1)
    if dt.weekday() == 0:
        monday += 1
        print(month)
