# Program that deals with Polymorphism and grteetings betwen different languages

# English Class
def greeting():
    return 'Hello!'


class English:
    def __init__(self):
        self.some_attribute = 'Default value'


def greeting():
    return 'Bonjour!'


class French:
    def __init__(self):
        self.some_attribute = 'Default value'


# Function for display
def greet(languages):
    print(languages.greeting())


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
