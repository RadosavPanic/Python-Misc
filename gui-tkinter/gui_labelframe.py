from tkinter import *

root = Tk()

labelFrame = LabelFrame(root, text="This is frame header")
labelFrame.pack(fill=BOTH, expand=YES)

lbl = Label(labelFrame, text="Label inside frame")
lbl.pack()

root.mainloop()
