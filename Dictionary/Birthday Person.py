# Program to find the birthday of a person

birthdays = {'Sachin': '03/14/2003',
             'Jacob': '09/05/1998',
             'Steven': '01/6/2001',
             'Liam': '02/03/1999',
             'Derrick': '06/22/2002'}

name = input('Enter a name to find the birthday: ')

if name in birthdays:
    print(birthdays[name])
else:
    print('Name was not found')
