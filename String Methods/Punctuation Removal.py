# Program that can remove the punctuations of a string

punctuation = "'!()-{}[]:;'*\,<>./?@#$%^&*_~"

s1 = input('Enter a string: ')
s2 = ''

for x in s1:
    if x not in punctuation:
        s2 += x

print(s2)


