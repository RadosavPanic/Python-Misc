from tkinter import  *

root = Tk()

text = Text(root)
text.insert(INSERT, "Hello....")
text.insert(END, "Bye bye...")
text.pack()

text.tag_add("here", "1.0", "1.5")
text.tag_add("start", "1.9", "1.12")
text.tag_config("here", background="green", foreground="white")
text.tag_config("start", background="gray", foreground="blue")

root.mainloop()
