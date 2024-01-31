# Program that functions as a regular stop watch, using Tkinter

from tkinter import *
import tkinter as tk
# Global variables
elapsedTime = 0
flag = False


# Start time function
def start_time():
    global elapsedTime, flag
    if not flag:
        flag = True
        update_time()


# Time display
def update_time():
    global elapsedTime, flag
    if flag:
        elapsedTime += 1
        sec = (elapsedTime // 1000) % 60
        minu = (elapsedTime // (1000 * 60)) % 60
        lbl1['text'] = f'{minu:02d}:{sec:02d}'
        lbl1.after(1, update_time)


# Stop time function
def stop_time():
    global flag
    flag = False


# Clear time function
def clear_time():
    global elapsedTime, flag
    elapsedTime = 0
    flag = False
    lbl1['text'] = '00:00'


# Window objects
win = tk.Tk()
win.title('Stop Watch')
win.geometry('1000x1000')

lbl1 = Label(win, bg='pink', text='00:00', font=('Times New Roman', 45))  # Label
lbl1.grid(row=0, column=1, columnspan=3)

# Grid manager
btn1 = Button(win, text='Start', bg='lightblue', fg='grey', command=start_time)  # Start Button
btn1.grid(row=1, column=1)

btn2 = Button(win, text='Stop', bg='lightblue', fg='grey', command=stop_time)  # Stop Button
btn2.grid(row=1, column=2)

btn3 = Button(win, text='Clear', bg='lightblue', fg='grey', command=clear_time)  # Clear Button
btn3.grid(row=1, column=3)

win.mainloop()
