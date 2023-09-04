from tkinter import messagebox
from tkinter import *

top = Tk()

var = StringVar()


def greet():
    messagebox.showinfo("Greeting", "Hello human! Your message element will update after you confirm.")
    var.set("Hello human!")


b1 = Button(top, text="Greet me!", relief=RAISED, command=greet)
b1.pack()
m1 = Message(top, textvariable=var, relief=RAISED); var.set("Text display here")
m1.pack()

top.mainloop()
