# Event class within Tkinter

from tkinter import *


def my_handler(e):
    print(e)


win = Tk()
win.title('Application')
win.geometry('600x400')

ent = Entry(win)
ent.pack()
ent.bind('<KeyPress>', my_handler)

win.mainloop()