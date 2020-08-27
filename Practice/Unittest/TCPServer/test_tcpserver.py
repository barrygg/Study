import unittest
import mock
from tcpserver import TcpServer


class Test_TcpServer(unittest.TestCase):
    @mock.patch('socket.socket')
    def test_srv(self, my_socket):
        my_socket = my_socket.return_value
        socket = mock.Mock()
        host = '127.0.0.1'
        srv = TcpServer(host=host, port=4444)

        my_socket.accept.return_value = (socket, host)
        socket.recv.return_value = "ABC123"

        assert srv._running == False

        srv.run()

        socket.send.assert_called_once_with("ABC123")
        socket.close.assert_called_once_with()
        my_socket.close.assert_called_once_with()
        assert srv._running == False


if __name__ == '__main__':
    unittest.main()
