from tkinter import messagebox
from tkinter import *

top = Tk()

c1 = Canvas(top, bg="blue", height=150, width=250)
coord = 0, 30, 220, 210
arc = c1.create_arc(coord, start=0, extent=150, fill="red")
c1.pack()

em = StringVar()

Label(top, text="User Name").pack()
e1 = Entry(top, bd=10, textvariable=em); em.set("")
e1.pack(); e1.focus()


def showText():
    if em.get() == "":
        messagebox.showwarning("Preview", "No text entered! Please enter your text.")
    else:
        messagebox.showinfo("Preview", em.get())


Button(top, text="Preview", command=showText).pack(side=BOTTOM)

top.mainloop()
