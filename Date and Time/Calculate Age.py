from datetime import datetime

# User input birthdate with clear format instruction
birthdate = input('Enter your birthdate (DD, MM, YYYY): ')

# Split the input and strip spaces
day, month, year = [int(part.strip()) for part in birthdate.split(',')]

# Create a date object for birthdate
bd = datetime(year, month, day)

# Current date
current_date = datetime.now()

# Calculate age
age = current_date - bd

print(age)
