# Tkinter Geometry widgets and their functionalities

from tkinter import *

# Creating an empty window
win = Tk()
win.title('Application')

# Pack manager
label1 = Label(win, text='Label 1', bg='pink', fg='black')  # Label 1
label1.pack(fill=Y, side=LEFT, padx=2, pady=2, ipadx=5)

label2 = Label(win, text='Label 2', bg='pink', fg='black')  # Label 2
label2.pack(fill=X, side=TOP, padx=2, pady=2, ipadx=5)

label3 = Label(win, text='Label 3', bg='pink', fg='black')  # Label 3
label3.pack(side=RIGHT, padx=2, pady=2, ipadx=5)

win.mainloop()
