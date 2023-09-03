import socket

socketObj = socket.socket()

host = socket.gethostname()
port = 12345

socketObj.connect((host, port))

print(socketObj.recv(1024).decode())

socketObj.close()
