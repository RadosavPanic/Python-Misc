from tkinter import *

root = Tk()

var = IntVar()


def select():
    text = optionList[var.get()-1]
    selection = f"You selected: {text}"
    labelBottom.config(text=selection)


optionList = ["Django", "Express.js", "Laravel"]

labelTop = Label(root, text="What's the best framework for web developers?")
r1 = Radiobutton(root, text="Django", variable=var, value=1, command=select)
r2 = Radiobutton(root, text="Express.js", variable=var, value=2, command=select)
r3 = Radiobutton(root, text="Laravel", variable=var, value=3, command=select)
labelBottom = Label(root)

labelTop.pack(); r1.pack(anchor=W);r2.pack(anchor=W);r3.pack(anchor=W);labelBottom.pack()

root.mainloop()
