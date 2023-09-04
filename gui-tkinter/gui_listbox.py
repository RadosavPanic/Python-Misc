from tkinter import *

top = Tk()

plList = ["Python", "Perl", "C", "PHP", "JSP", "Ruby"]

lb1 = Listbox(top, selectmode=SINGLE)

for i in range(len(plList)):
    lb1.insert(i, plList[i])

lb1.activate(1)
lb1.select_set(1, 1)
lb1.pack()

top.mainloop()
