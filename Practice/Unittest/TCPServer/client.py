import socket
host = '127.0.0.1'
port = 5556
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
s.send('hello'.encode())
data = s.recv(1024).decode()
print('Ответ сервера:', data)
s.close()

