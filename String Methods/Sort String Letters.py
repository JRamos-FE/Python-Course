# Program that can sort the letters of a string

s = input('Enter a string: ')

sort = sorted(s)
s_sort = ''.join(sort)
print(s_sort)