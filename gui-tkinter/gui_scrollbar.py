from tkinter import *

root = Tk()

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

lb = Listbox(root, yscrollcommand=scrollbar.set)

for line in range(30):
    lb.insert(END, f"This is line ({str(line + 1)})")

lb.pack(side=LEFT, fill=BOTH)

scrollbar.config(command=lb.yview)

root.mainloop()
