# Program that can provide the sum of scores of only the elements that end in zero

# List of scores
scores = [200, 456, 300, 10, 234, 678]


# Function
def sum_zero(L):
    # Variable to sum
    sum_num_end_zero = 0
    for x in L:
        # Iterate through
        if x % 10 == 0:
            sum_num_end_zero += x
    return sum_num_end_zero


# Declaring the function
x = sum_zero(scores)
print(x)
