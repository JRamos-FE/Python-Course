# Brief code on Widgets and their functionalities

from tkinter import *

win = Tk()
win.title('Application 1')
win.geometry('600x400+100+100')

l = Checkbutton(win, text='Hello World', width=100, variable='var')

l['justify'] = 'right'
l['bd'] = 3
l['bg'] = 'red'
l['bg'] = 'pink'

l.config(font='Ariel, 10', height=100)

l.pack(pady=100)
win.mainloop()
