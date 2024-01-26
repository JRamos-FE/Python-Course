# Program that deals with array data structures
# Finding the first duplicate element in an array

import array

# Array
nums = array.array('i', [10, 20, 13, 14, 15, 13, 17, 10, 20, 13])


# Finding duplicate functions
def find_duplicate(element_array):
    holder = []
    for element in element_array:
        if element not in holder:
            holder.append(element)
        elif element in holder:
            return element
        else:
            return 'Invalid'


print(find_duplicate(nums))

