# Event is any action that is done by the user through interaction with widgets of the application
# An event handler is the function that responds to the event
# The method used is called binding

from tkinter import *


# Function for button 1 event handling
def fun(msg):
    print(msg)


win = Tk()
win.title('Application')
win.geometry('600x600')

b1 = Button(win, text='My Button', command=lambda: fun('Button is clicked!!')) # Taken with lambda for parameter
b1.pack()

win.mainloop()
