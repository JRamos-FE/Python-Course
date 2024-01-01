# Program that deals with Polymorphism and grteetings betwen different languages

# English Class
class English:
    def __init__(self):
        self.some_attribute = 'Default value'

    def greeting(self):
        return 'Hello!'
    
class French:
    def __init__(self):
        self.some_attribute = 'Default value'
    
    def greeting(self):
        return 'Bonjour!'
    
# Function for display
def greet(language):
    print(language.greeting())

# Input selection and display
language_selected = input('Enter the language (English or French): ').lower()
language = None

if language_selected == 'english':
    language = English()
elif language_selected == 'french':
    language = French()

if language:
    greet(language)
else:
    print('Invalid language selection')