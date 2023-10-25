# Program that will take a function to call an ID and provide the corresponding planet associated

# Taking user input
planet_id = int(input('Enter an ID: '))

# Creating the dictionary
planets = {
    1: 'Mercury',
    2: 'Venus',
    3: 'Earth',
    4: 'Mars',
    5: 'Jupiter',
    6: 'Saturn',
    7: 'Uranus',
    8: 'Neptune',
    9: 'Pluto'
}


# Function that iterates
def planet(ident):
    return planets[ident]


# Calling the function
planet(planet_id)
p = planet(id)
print('Planet name is: ', p)