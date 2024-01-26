# program that deals with deque rotation

from collections import deque

students = deque([1, 2, 3, 4,5, 6, 7, 8, 9, 10])


def serve():
    print('Initial Order: ', students)
    students.rotate(1)

serve()
serve()
serve()
serve()

