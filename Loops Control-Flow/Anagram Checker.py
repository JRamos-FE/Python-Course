# Program to check whether two strings are anagrams

s1 = input('Enter a string: ')
s2 = input('Enter another string: ')

if len(s1) != len(s2):
    print('Not an anagram')
else:
    for x in s1:
        if x not in s2:
            print('Not an anagram')
            break;
    else:
        print('Anagram!')
