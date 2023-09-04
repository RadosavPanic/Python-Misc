from tkinter import *

top = Tk()

CheckVar1 = IntVar(); CheckVar2 = IntVar()


def isClicked():
    print(CheckVar1.get())


c1 = Checkbutton(top, bg="yellow", text="Music", variable=CheckVar1,
                 onvalue=1, offvalue=0, height=5, width=20, command=isClicked)

c2 = Checkbutton(top, text="Video", variable=CheckVar2, onvalue=1, offvalue=0, height=5, width=20)

c1.pack(); c2.pack()

top.mainloop()


