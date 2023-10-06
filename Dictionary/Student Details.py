# Program that contains the details of students using dictionary inputs

# Empty dictionary; students is primary and info for what goes inside as values
students = {}

# Taking in the name of each student that will be added
name = input('Enter student name: ')

# Loop to find whether the student name is already created and inclusion into the dictionary
if name not in students:
    students[name] = {}

# Info for the values of each student
roll_num = input('Enter students roll number: ')
dept_name = input('Enter students department: ')

# Nested dictionary
info = students[name]
info['Roll Number: '] = roll_num
info['Department Name: '] = dept_name

# Printing the dictionary
print(students)

