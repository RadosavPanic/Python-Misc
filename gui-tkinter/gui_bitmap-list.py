from tkinter import *

top = Tk()

b1 = Button(top, relief=RAISED, bg="red", fg="white", bitmap="error")
b2 = Button(top, relief=RAISED, bg="black", fg="yellow", bitmap="hourglass")
b3 = Button(top, relief=RAISED, bg="blue", fg="white", bitmap="info")
b4 = Button(top, relief=RAISED, bg="gray", fg="red", bitmap="question")
b5 = Button(top, relief=RAISED, bg="white", fg="red", bitmap="warning")
b6 = Button(top, relief=RAISED, bg="white", fg="blue", bitmap="questhead")

buttonsList = [b1, b2, b3, b4, b5, b6]

for btn in buttonsList:
    btn.pack(side=LEFT)

top.mainloop()
