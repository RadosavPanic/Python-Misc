from tkinter import messagebox
from tkinter import *

top = Tk()


def greet():
    messagebox.showinfo("Greeting", "Hello human!")


b1 = Button(top, text="Greet me!", relief=RAISED, command=greet)
b1.pack()
b1.place(height=100, width=100)

top.mainloop()
