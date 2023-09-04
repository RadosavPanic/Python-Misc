from tkinter import *


def showVal():
    selection = f"Value: {var.get()}"
    label.config(text=selection)


root = Tk()

var = DoubleVar()
scale = Scale(root, variable=var)
scale.pack(anchor=CENTER)
btn = Button(root, text="Get Scale Value", command=showVal)
btn.pack(anchor=CENTER)
label = Label(root)
label.pack()

root.mainloop()
