import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 12345
s.connect((host, port))
message = input('Enter your message: ')
s.send(message.encode())
data = s.recv(1024)
print('Got data from server: {}'. format(data.decode()))
s.close()


