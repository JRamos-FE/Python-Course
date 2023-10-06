# Program that can sort and display countries names in alphabetical order

name = input('Enter a country name: ')

countries = {}

letterCountry = name[0].upper()

if letterCountry not in countries:
    countries = [name]
else:
    countries[letterCountry].append(name)

print(countries)