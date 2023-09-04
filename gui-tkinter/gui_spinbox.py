from tkinter import *

top = Tk()


def showVal():
    selection = f"Value: {var.get()}"
    label.config(text=selection)


var = StringVar()
sb = Spinbox(top, from_=0, to=10, command=showVal, textvariable=var)
sb.pack()

label = Label(top)
label.pack()

top.mainloop()
