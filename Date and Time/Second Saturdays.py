from datetime import datetime, timedelta


def second_saturdays(year):
    second_sat_list = []

    for month in range(1, 13):  # Iterate through each month
        # Set the date to the first of the month
        d = datetime(year, month, 1)

        # Find the first Saturday
        days_to_sat = (5 - d.weekday() + 7) % 7
        first_sat = d + timedelta(days=days_to_sat)

        # The second Saturday will be 7 days after the first Saturday
        second_sat = first_sat + timedelta(days=7)

        # Add to the list
        second_sat_list.append(second_sat.strftime('%Y-%m-%d'))

    return second_sat_list


# User input
user_year = int(input('Year: '))
sec_sat_list = second_saturdays(user_year)

# Print list
for saturday in sec_sat_list:
    print(saturday)
