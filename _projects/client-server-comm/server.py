from tkinter import *
import socket
import threading
import time


def server():
    s = socket.socket()
    host = socket.gethostname()
    port = 12345
    s.bind((host, port))
    s.listen(5)
    while True:
        lb.insert(0, "SERVER: Waiting...")
        conn, addr = s.accept()
        message = conn.recv(1024).decode()
        lb.insert(0, message)
        response = ""

        if message.__contains__("TIME"):
            response += "Time: " + time.strftime('%H:%M:%S', time.localtime())
        if message.__contains__("END"):
            response += "Animation stopped"

        conn.send(response.encode())


root = Tk()

lb = Listbox(root, width=40, height=20)
lb.pack()

thread1 = threading.Thread(target=server)
thread1.start()

root.mainloop()
