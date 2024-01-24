# Program that will display an inner and outer course accordingly

# Outer class course
class Course:
    def __init__(self, course_name, course_duration, *books):
        self.book = None
        self.course_name = course_name
        self.course_duration = course_duration
        self.books = [self.Book(title) for title in books]

    def show_details(self):
        print(f'Course: {self.course_name}')
        print(f'Course Duration: {self.course_duration}')
        print(f'Book: {self.book}')

    class Book:
        def __init__(self, title, author, publication_date):
            self.title = title
            self.author = author
            self.publication_date = publication_date

        def __str__(self):
            return f"Title: {self.title}\nAuthor: {self.author}\nPublication Date: {self.publication_date}"
