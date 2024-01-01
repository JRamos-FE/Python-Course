# Progam that relates to polymorphism and pets

# Cat class
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def info(self):
        info = f'Name: {self.name}\n Age: {self.age}'
        return info
    
    def make_sound(self):
        return 'Meow Meow'

# Dog class    
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        info = f'Name: {self.name}\n Age: {self.age}'
        return info

    def make_sound(self):
        return 'Woof Woof'

# Function for pet type display
def my_pet(pet):
    print(pet.info())
    print(pet.make_sound())

# Input selection and display
pet_type = input('Enter your pets type (dog or cat): ').lower()
pet = None

if pet_type == 'dog':
    name = input('Enter your dogs name: ')
    age = input('Enter your dogs age: ')
    pet = Dog(name, age)
elif pet_type == 'cat':
    name = input('Enter your cats name: ')
    age = input('Enter your cats age: ')
    pet = Cat(name, age)

if pet:
    my_pet(pet)
else:
    print('Invalid pet type')


