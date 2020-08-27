# write your code here
import socket
import sys


s = sys.argv
address = (s[1], int(s[2]))
data = s[3]
hacker = socket.socket()
hacker.connect(address)
hacker.send(data.encode())
response = hacker.recv(1024)
print(response.decode())
