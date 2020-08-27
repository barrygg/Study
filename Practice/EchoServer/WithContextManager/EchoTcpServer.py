import socket


class EchoTcpServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    def __enter__(self):
        self._socket.bind((self.host, self.port))
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        self._socket.close()
    def listen(self):
        while True:
            self._socket.listen(5)
            conn, addr = self._socket.accept()
            data = conn.recv(1024).decode()
            print(data)
            conn.send(data.encode())



with EchoTcpServer('127.0.0.1', 12345) as srv:
    srv.listen()
        
