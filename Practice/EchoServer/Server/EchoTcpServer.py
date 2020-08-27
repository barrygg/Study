import socket
import threading


class ClientThread(threading.Thread):
    def __init__(self, conn, addr):
        super().__init__()
        self._connection = conn
        self._address = addr
    def run(self):
        print('Connection from address {}'.format(self._address))
        data = self._connection.recv(1024)
        print('Received {}'.format(data.decode()))
        self._connection.send(data)
        self._connection.close()
        print('Closed connection from {}'.format(self._address))


class EchoTcpServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self._socket = None
        self._running = False
    def run(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._socket.bind((self.host, self.port))
        self._socket.listen(5)
        self._runnning = True
        print('Server is up')
        while self._running:
            try:
                conn, addr = self._socket.accept()
                ClientThread(conn, addr).start()
            except Exception:
                self._running = False
    def stop(self):
        self._running = False
        self._socket.close()
        print('Server is down')

if __name__ == '__main__':
    srv = EchoTcpServer(host='127.0.0.1', port=5555)
    try:
        srv.run()
    except KeyboardInterrupt:
        srv.stop()