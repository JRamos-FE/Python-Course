# Importing modules
import sqlite3

conn = sqlite3.connect('univ.db')

cur = conn.cursor()

# Number of students
num_students = int(input('Enter the amount of students: '))

# Loop to input student data
for _ in range(num_students):
    roll = input("Enter roll number: ")
    name = input("Enter name: ")
    city = input("Enter city: ")
    dept_no = input("Enter department number: ")

    # SQL INSERT statement
    insert_stmt = '''INSERT INTO students (rollnum, name, city, deptno)
                     VALUES (?, ?, ?, ?)'''
    cur.execute(insert_stmt, (roll, name, city, dept_no))

conn.commit()

cur.close()

conn.close()