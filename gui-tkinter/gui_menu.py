from tkinter import *


def donothing():
    tl = Toplevel(root)
    btn = Button(tl, textvariable="Do nothing button")


root = Tk()

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)
fileLabelsList = ["New", "Open", "Save", "Save as", "Close"]
for idx in range(len(fileLabelsList)):
    filemenu.add_command(label=fileLabelsList[idx], command=donothing)

filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

editmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=editmenu)

editLabelsList = ["Undo", "Cut", "Copy", "Paste", "Delete", "Select All"]

for idx in range(len(editLabelsList)):
    if idx == 1:
        editmenu.add_separator()
    editmenu.add_command(label=editLabelsList[idx], command=donothing)

helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="Contact", command=donothing)
helpmenu.add_command(label="About", command=donothing)

root.config(menu=menubar)

root.mainloop()
