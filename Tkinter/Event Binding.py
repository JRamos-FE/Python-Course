# Event binding

# Event types
# Activate = Widget became active
# Button = Mouse button pressed
# ButtonRelease = Mouse button released
# Configure = Size of the widget is changed
# Deactivate = Widget Deactivated
# Destroy = Widget is destroyed
# Enter = Mouse pointer entering on widget
# Expose = Widget become visible
# FocusIn = Widget is highlighted
# FocusOut = Widget is dehilighted
# KeyPress = A keyboard key is pressed
# KeyRelease = A keyboard key is released
# Leave = Mouse pointer leaving from widget
# Motion = Mouse pointer moving upon widget
# MouseWheel = Mouse scrolling
# Visibility = Widget is visible

from tkinter import *
from tkinter.messagebox import *


def fun(e):
    showinfo('My Box: ', 'Event is generated')


win = Tk()
win.title('Application')
win.geometry('600x400')

e = Entry(win, bg='red', fg='yellow')
e.place(x=100, y=100, width=200, height=50)

e1 = Entry(win, bg='red', fg='yellow')
e1.place(x=100, y=150, width=200, height=50)

# e.bind('<Button>', fun)
# e1.bind('<Button>', fun), instance based

# win.bind_class('Entry', '<Button>', fun)  // Class level binding
win.bind_all('<Button>', fun)  # Application level binding

win.mainloop()
