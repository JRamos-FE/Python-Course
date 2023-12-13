# Program that displays employee info and tracks the count, using a class

# Employee class
class Employee:
    employee_count = 101 # Class variable count

    def __init__(self, name, salary, designation):
        self.name = name
        self.salary = salary
        self.emp_id = str(Employee.employee_count)
        self.designation = designation
        Employee.employee_count += 1

    def show_details(self):
        details = f'Name: {self.name}, Salary: ${self.salary}, ID: e{self.emp_id}, Designation: {self.designation}'
        return details
    
    def total_emp(cls):
        return cls.employee_count - 101
    
# Creating an employee
employee_1 = Employee("Rohit", 120000, 'QA Engineer')
print(employee_1.show_details())

# Creating another employee
employee_2 = Employee("James", 100000, 'Back End Engineer')
print(employee_2.show_details())

# Calling the count function
print(f'Toatl Employees: {employee_1.total_emp()}')
