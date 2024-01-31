# Program dealing with Tkinter to create a clock that displays the current time and runs
import time
from tkinter import *


# Clock local time function
def clock_time():
    lbl1['text'] = time.strftime('%H:%M:%S', time.localtime())
    lbl1.after(100, clock_time)


# Creating window object
win = Tk()
win.title = 'Clock'
win.geometry = '1000x1000'

lbl1 = Label(win, bg='pink', text='grey', font=('Times New Roman', 30))
lbl1.pack(fill=BOTH, expand=TRUE)

clock_time()
win.mainloop()