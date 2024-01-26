# Program that can identify a missing natural number from an array

import array

# Array of integers
nums = array.array('i', [1, 3, 4, 5, 6, 7, 8, 9, 10])


# Function that finds missing natural number
def missing_natural(nums_array):
    # First and last number in the array
    first_num = nums_array[0]
    last_num = nums_array[-1]

    # List matching the range of the array
    nums_list = list(range(first_num, last_num + 1))

    # Iteration through elements to verify missing number
    for x in nums_list:
        if x in nums_array:
            continue
        else:
            return 'Missing number is: ', x


# Printing result
result = missing_natural(nums)
print(result)
