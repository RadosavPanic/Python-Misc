from tkinter import *
from tkinter.font import Font

top = Tk()

fontVerdana = Font(top, family="Verdana", size=12, weight="bold", slant="roman", underline=True)

l1 = Label(top, text="Verdana", font=fontVerdana)
l2 = Label(top, text="Arial", font=("Arial", 18))
l1.pack(); l2.pack()

b1 = Button(top, text="FLAT", relief=FLAT)
b2 = Button(top, text="RAISED", relief=RAISED)
b3 = Button(top, text="SUNKEN", relief=SUNKEN)
b4 = Button(top, text="GROOVE", relief=GROOVE)
b5 = Button(top, text="RIDGE", relief=RIDGE)

buttonsList = [b1, b2, b3, b4, b5]

for btn in buttonsList:
    btn.pack()

top.mainloop()
