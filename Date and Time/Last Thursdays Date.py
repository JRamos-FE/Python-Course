from datetime import datetime, timedelta

# User input
given_date = input('Enter a date (dd-mm-yyyy): ')


# Function to find last Thursday
def find_last_thursday(str_date):
    # Converting the string to datetime object
    # Ensure the format here matches the expected input format
    user_date = datetime.strptime(str_date, '%d-%m-%Y')

    # Find the weekday number (Note: Monday = 0)
    weekday_num = user_date.weekday()

    # Calculate last Thursday difference (Note: Thursday = 3)
    days_last_thursday = weekday_num - 3

    # Loop iteration if given date is before Thursday, subtract a week
    if days_last_thursday < 0:
        days_last_thursday += 7

    # Calculate the last Thursday's date
    latest_thursday = user_date - timedelta(days=days_last_thursday)
    return latest_thursday


# Find and print last Thursday
last_thursday = find_last_thursday(given_date)
print("The last Thursday's date: ", last_thursday.strftime('%d-%m-%Y'))
