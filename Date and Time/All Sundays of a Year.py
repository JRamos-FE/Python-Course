# Program that can find all the Sundays of an inputted year

# Importing modules
from datetime import datetime, timedelta


# Function to find all the Sundays for the year
def find_sundays(given_year):
    # First day of that year
    d1 = datetime(given_year, 1, 1)

    # First Sunday of the year (Note: Sunday = 6)
    days_to_sunday = 6 - d1.weekday()
    if days_to_sunday != 6:
        d1 += timedelta(days=days_to_sunday)

    # List for Sundays
    sundays = []

    # Iterate through year
    while d1.year == given_year:
        sundays.append(d1.strftime('%Y-%m-%d'))
        d1 += timedelta(days=7)  # Next Sunday

    return sundays


# User input
user_year = int(input('Enter a given year: '))
sunday_list = find_sundays(user_year)

# Print list of Sundays
for sunday in sunday_list:
    print(sunday)

