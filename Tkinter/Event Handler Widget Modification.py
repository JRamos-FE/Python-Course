# Example of how an even handler can modify the attributes of a widget

from tkinter import *
from tkinter.messagebox import *


def my_handler(e):
    if int(e.type) == 7:
        lbl['bg'] = 'pink'
        lbl['text'] = 'pink'
    elif int(e.type) == 8:
        lbl['bg'] = 'red'
        lbl['text'] = 'red'


def my_handler2(e):
    lbl['bg'] = 'red'
    lbl['text'] = 'red'


win = Tk()
win.title('Application')
win.geometry('600x400')

lbl = Label(win, text='blue color', bg='blue', width=20, height=20)
lbl.pack()
lbl.bind('<Enter>', my_handler)
lbl.bind('<Leave>', my_handler2, add='+')

win.mainloop()
