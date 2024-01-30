# Tkinter Geometry widgets and their functionalities

from tkinter import *

# Creating an empty window
win = Tk()
win.title('Application')

# Grid manager
button1 = Button(win, text='Button 1', bg='lightblue', fg='grey')  # Button 1
button2 = Button(win, text='Button 2', bg='lightblue', fg='grey')  # Button 2
button3 = Button(win, text='Button 3', bg='lightblue', fg='grey')  # Button 3
button4 = Button(win, text='Button 4', bg='lightblue', fg='grey')  # Button 4
button5 = Button(win, text='Button 5', bg='lightblue', fg='grey')  # Button 5
button6 = Button(win, text='Button 6', bg='lightblue', fg='grey')  # Button 6
button7 = Button(win, text='Button 7', bg='lightblue', fg='grey')  # Button 7
button8 = Button(win, text='Button 8', bg='lightblue', fg='grey')  # Button 8
button9 = Button(win, text='Button 9', bg='lightblue', fg='grey')  # Button 9

button1.grid(row=0, column=0, padx=5, pady=5)
button2.grid(row=0, column=1, padx=5, pady=5)
button3.grid(row=0, column=2, padx=5, pady=5)

button4.grid(row=1, column=0, padx=5, pady=5)
button5.grid(row=1, column=1, padx=5, pady=5)
button6.grid(row=1, column=2, padx=5, pady=5)

button7.grid(row=2, column=0, padx=5, pady=5)
button8.grid(row=2, column=1, padx=5, pady=5)
button9.grid(row=2, column=2, padx=5, pady=5)

win.mainloop()
