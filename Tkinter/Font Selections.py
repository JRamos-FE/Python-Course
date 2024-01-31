# Program that deals with Tkinter that forms a selection of fonts and displays the text within the label according to
# selection

from tkinter import *
import tkinter as tk
from tkinter.font import *


# Update label function
def update_label():
    b = ['bold' if varBold.get() == 1 else 'normal'][0]
    i = ['italic' if varItalic.get() == 1 else 'roman'][0]
    fnt = Font(family='Times New Roman', size=45, weight=b, slant=i, underline=varUnderline.get())
    lbl1['font'] = fnt


win = tk.Tk()
win.title('Font Selections')
win.geometry('1000x1000')

lbl1 = Label(win, bg='pink', text='Hello World!', font=('Times New Roman', 45))  # Label
lbl1.grid(row=0, column=1, columnspan=3)

varBold = IntVar(value=0)  # Bold button
cb1 = Checkbutton(win, text='Bold', onvalue=1, offvalue=0, variable=varBold, command=update_label)
cb1.grid(row=1, column=0)

varItalic = IntVar(value=0)  # Italic button
cb2 = Checkbutton(win, text='Italic', onvalue=1, offvalue=0, variable=varItalic, command=update_label)
cb2.grid(row=1, column=1)

varUnderline = IntVar(value=0)  # Underline button
cb3 = Checkbutton(win, text='Underline', onvalue=1, offvalue=0, variable=varUnderline, command=update_label)
cb3.grid(row=1, column=2)

win.mainloop()
