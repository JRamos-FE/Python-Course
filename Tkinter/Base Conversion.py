import tkinter as tk

# Window objects
win = tk.Tk()
win.title('Base Conversion')
win.geometry('1000x1000')

# Global variable that manages the button selection
var = tk.IntVar(value=0)
value = 25  # The value to be converted


# Update the label function
def update_label():
    global value
    if var.get() == 0:
        lbl1['text'] = str(value)
    elif var.get() == 1:
        lbl1['text'] = str(bin(value))
    elif var.get() == 2:
        lbl1['text'] = str(oct(value))
    elif var.get() == 3:
        lbl1['text'] = str(hex(value))


# Label
lbl1 = tk.Label(win, bg='pink', text=str(value), font=('Times New Roman', 45))
lbl1.grid(row=0, column=1, columnspan=4)

# Radiobutton grid
btn1 = tk.Radiobutton(win, text='Decimal', bg='lightblue', fg='grey', variable=var, value=0, command=update_label)
btn1.grid(row=1, column=0)

btn2 = tk.Radiobutton(win, text='Binary', bg='lightblue', fg='grey', variable=var, value=1, command=update_label)
btn2.grid(row=1, column=1)

btn3 = tk.Radiobutton(win, text='Octal', bg='lightblue', fg='grey', variable=var, value=2, command=update_label)
btn3.grid(row=1, column=2)

btn4 = tk.Radiobutton(win, text='Hexa', bg='lightblue', fg='grey', variable=var, value=3, command=update_label)
btn4.grid(row=1, column=3)

win.mainloop()
