# Program that utilzies a function for Pascal's Triangle
# Pascal's Triangle Formula (n + 1)C(r) = (n)C(r - 1) + (n)C(r)

# User input
n = int(input('Enter how many rows you want: '))

# Function creation
def pascal_triangle(rows):
    row = [1]
    for i in range(n):
        print(row)
        temp_row = [0] + row
        row = row + [0]
        new_row = [x + y for x, y in zip(row, temp_row)]       
        row = new_row

# Calling the function
pascal_triangle(n)