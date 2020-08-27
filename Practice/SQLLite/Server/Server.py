import socket
import sqlite3


conn = sqlite3.connect('sqlite.db')
conn.execute('CREATE TABLE COMPANY'
' (ID INT PRIMARY KEY NOT NULL,'
' NAME TEXT NOT NULL,'
' AGE INT NOT NULL,'
' ADDRESS CHAR(50),'
' SALARY REAL);')
conn.execute("INSERT INTO COMPANY (ID, NAME, AGE, ADDRESS, SALARY)"
"VALUES (1, 'Paul', 32, 'California', 20000.00)")
conn.execute("INSERT INTO COMPANY (ID, NAME, AGE, ADDRESS, SALARY)"
"VALUES (2, 'Allen', 25, 'Texas', 15000.00)")
conn.execute("INSERT INTO COMPANY (ID, NAME, AGE, ADDRESS, SALARY)"
"VALUES (3, 'Teddy', 23, 'Norway', 20000.00)")
conn.execute("INSERT INTO COMPANY (ID, NAME, AGE, ADDRESS, SALARY)"
"VALUES (4, 'Mark', 25, 'Richmond', 65000.00)")
conn.commit()


# Server sends to client result of SQL query
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 12345
s.bind((host, port))
s.listen(5)
while True:
    connect, addr = s.accept()
    print('Server got the connection. Address = {}'.format(addr))
    item = int(connect.recv(1024).decode())
    print('Server got id from client: {}'.format(item))
    cursor = conn.execute("SELECT name, age, address, salary from COMPANY WHERE id = '%s'" %item)
    data = ' '.join(map(str, cursor.fetchone()))
    connect.send(data.encode())
    connect.close()
