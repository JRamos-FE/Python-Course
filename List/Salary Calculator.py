# Program to find the amount of salary that an employee makes based on the hours worked per day of the week

mon_hours = int(input('Enter Monday Hours: '))
tues_hours = int(input('Enter Tuesday Hours: '))
wed_hours = int(input('Enter Wednesday Hours: '))
thurs_hours = int(input('Enter Thursday Hours: '))
fri_hours = int(input('Enter Friday Hours: '))

hours_list = []
hours_list.extend([mon_hours,tues_hours,wed_hours,thurs_hours,fri_hours])

hours_total = sum(hours_list)

wage = int(input('Enter your hourly wage: '))

salary = hours_total * wage
print('Your weekly salary = ', salary)