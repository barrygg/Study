import socket
import string


def decoder(s):
    alphabet = string.ascii_letters
    alphabet_r = string.ascii_lowercase[::-1] + string.ascii_uppercase[::-1]
    symbols = '@#$%^&*'
    transtab_r = str.maketrans(alphabet_r, alphabet, symbols)
    s = s.translate(transtab_r)
    return s


sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
host = '127.0.0.1'
port = 12345
sock.bind((host, port))
print ('Start Server')
while True:
    data, addr = sock.recvfrom(1024)
    print('Server got data from client: {}'.format(data.decode()))
    sock.sendto(decoder(data.decode()).encode(), addr)
# s.close()