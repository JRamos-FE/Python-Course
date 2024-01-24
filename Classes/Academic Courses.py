# Program that deals with inner classes and outer courses with academic courses as examples

# Outer class Course
class Course:
    def __init__(self, course_name, course_duration, *books):
        self.course_name = course_name
        self.course_duration = course_duration
        self.books = [self.Book(x) for x in books]

    def show_details(self):
        details = f'Course: {self.course_name}\n Duration: {self.course_duration} hours\n'
        for book in self.books:
            details += f'- {book}\n'
        return details

    # Inner class Book    
    class Book:
        def __init__(self, title):
            self.title = title

        def __str__(self):
            return self.title


# Creating and calling an object
coruse1 = Course('Python', 20, 'Math for Programmers', 'Python for Beginners')
print(coruse1.show_details())
