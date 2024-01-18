from datetime import datetime


def day_of_year(date_str):
    # Convert the input string to datetime object
    user_date = datetime.strptime(date_str, '%d-%m-%Y')

    # Start date of the year
    start_of_year = datetime(user_date.year, 1, 1)

    # Calculate difference
    diff = user_date - start_of_year

    # Add 1 because timedelta starts counting from 0
    return diff.days + 1


# Get user input
input_date = input("Enter the date (dd-mm-yyyy): ")

# Calculate and print the day of the year
day_num = day_of_year(input_date)
print(f"The day number of the year for {input_date} is: {day_num}")
