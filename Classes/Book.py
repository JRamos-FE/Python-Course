# Program that can display properties of a book with a class

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def show_details(self):
        details = f'Title: {self.title}, Author: {self.author}, Price: ${self.price}'
        return details


b1 = Book('GEB', "Douglas Hofstadter", 20)
print(b1.show_details())
