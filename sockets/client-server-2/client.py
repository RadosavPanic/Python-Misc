# Echo client program

import socket

host = '127.0.0.1'
port = 50007

socketObj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socketObj.connect((host, port))

socketObj.send(b'Hello from client1')
data = socketObj.recv(1024)
socketObj.close()
print(f'Received: {data}')


