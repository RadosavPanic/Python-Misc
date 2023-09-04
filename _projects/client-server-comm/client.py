from tkinter import *
import time
import socket
import threading

stop = False


def client():
    global stop

    s = socket.socket()
    host = socket.gethostname()
    port = 12345

    if len(entry.get()) > 0:
        s.connect((host, port))
        passText = ""
        passText += f"{entry.get()}:{rbVar.get()}"
        s.send(passText.encode())
        resp = s.recv(1024).decode()
        lb.insert(0, resp)

        if resp.__contains__("Animation stopped"):
            stop = True
        s.close()


def animation():
    arc = canvas.create_arc(20, 20, 280, 150, start=0, extent=180, fill="red")
    angle = 0
    while True:
        line = canvas.create_arc(20, 20, 280, 150, start=0, extent=angle)
        angle += 10
        if angle == 190:
            angle = 0
        time.sleep(0.2)
        canvas.delete(line)
        if stop:
            canvas.delete(arc)
            break

    angle = 180
    while True:
        arc = canvas.create_arc(20, 20, 280, 150, start=0, extent=angle, fill="red")
        angle -= 10
        time.sleep(0.2)
        canvas.delete(arc)
        if angle == -10:
            break


root = Tk()

canvas = Canvas(root, width=300, height=200, bg="gray")
canvas.pack()

name = Label(root, text="Name", bg="green", fg="white")
name.pack()

entry = Entry(root)
entry.pack()

rbVar = StringVar()
rbTime = Radiobutton(root, variable=rbVar, text="Time", value="TIME")
rbTime.pack()
rbEnd = Radiobutton(root, variable=rbVar, text="End", value="END")
rbEnd.pack()

btnSend = Button(root, text="Send", command=client)
btnSend.pack()

lb = Listbox(root, width=30, height=15)
lb.pack()

threadAnimation = threading.Thread(target=animation)
threadAnimation.start()

root.mainloop()
