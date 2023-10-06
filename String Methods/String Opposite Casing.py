# Program that converts that characters of a string to opposite characterization

s1 = input('Enter a string: ')

lower = ''
upper = ''

for x in s1:
    if x.islower():
        lower += x
    else:
        upper += x

s2 = lower + upper

print(s2)