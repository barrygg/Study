import socket
import string
import random


def coder(s):
    alphabet = string.ascii_letters
    alphabet_r = string.ascii_lowercase[::-1] + string.ascii_uppercase[::-1]
    symbols = '@#$%^&*'
    transtab = str.maketrans(alphabet, alphabet_r)
    s = s.translate(transtab)
    for j in [random.randint(0, len(s) - 1) for i in range(random.randint(0, len(s) -1))]:
        s = s[:j] + random.choice(symbols) + s[j:]
    return s


message = coder(input('Enter your message: '))


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = '127.0.0.1'
port = 12345
sock.sendto(message.encode(), (host, port))
data, addr = sock.recvfrom(1024)
print(data.decode())
sock.close()