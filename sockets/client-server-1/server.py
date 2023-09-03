import socket

socketObj = socket.socket()  # socket(domain, type, protocol=0)

host = socket.gethostname()
port = 12345

socketObj.bind((host, port))
socketObj.listen(5)

while True:
    conn, addr = socketObj.accept()
    print(f"Got connection from {addr}")
    messageToClient = "Server: connection established successfully."
    conn.send(messageToClient.encode())
    conn.close()

