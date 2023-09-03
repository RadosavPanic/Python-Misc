# Echo client program

import socket

port = 50007
host = ''

socketObj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socketObj.bind((host, port))
socketObj.listen(1)

while True:
    conn, addr = socketObj.accept()
    print(f"Connected with {addr}")
    data = conn.recv(1024)
    if not data:
        break
    conn.send(data)
    conn.close()

