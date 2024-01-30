# Tkinter Geometry widgets and their functionalities

from tkinter import *

# Creating an empty window
win = Tk()
win.title('Application')
win.geometry('800x600')

# Place manager
button1 = Button(win, text='Button 1', bg='pink', fg='grey')
button2 = Button(win, text='Button 2', bg='pink', fg='grey')
button3 = Button(win, text='Button 3', bg='pink', fg='grey')


button1.place(x=100, y=100, width=150, height=100)
button2.place(x=260, y=200, width=150, height=100)
button3.place(relx=.8, rely=.8, relwidth=.15, relheight=.1) # This button is set with relative notation


win.mainloop()
