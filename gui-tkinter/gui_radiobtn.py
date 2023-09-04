from tkinter import *

root = Tk()

var = IntVar()


def select():
    text = optionList[var.get() - 1]
    selection = f"You selected: {text}"
    labelBottom.config(text=selection)


optionList = ["Django", "Express.js", "Laravel"]

Label(root, text="What's the best framework for web developers?").pack()
for idx in range(3):
    Radiobutton(root, text=optionList[idx-1], variable=var, value=idx, command=select).pack()
labelBottom = Label(root)
labelBottom.pack()

root.mainloop()
