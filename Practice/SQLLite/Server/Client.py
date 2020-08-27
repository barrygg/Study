import socket
import random


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 12345
s.gettimeout()
s.connect((host, port))
message = str(random.randint(1,4))
s.send(message.encode())
data = s.recv(1024)
print('Got data from server: {}'. format(data.decode()))
s.close()