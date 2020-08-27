import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 12345
s.bind((host, port))
s.listen(5)
while True:
    conn, addr = s.accept()
    print('Connection from address {}'.format(addr))
    data = conn.recv(1024).decode()
    print('Received {}'.format(data))
    conn.send(data.encode())
    conn.close()
s.close()    
