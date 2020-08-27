import socket


class TcpServer:
    def __init__(self, host, port):
        self._host = host
        self._port = port
        self._running = False

    def run(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((self._host, self._port))
        s.listen(1)

        self._running = True
        conn, addr = s.accept()
        print('Подключения с этого адреса :', addr)
        data = conn.recv(1024)
        print('Ответ :', data)
        conn.send(data)
        conn.close()
        self._running = False

        s.close()


if __name__ == '__main__':
    srv = TcpServer("127.0.0.1", 5556)
    srv.run()
