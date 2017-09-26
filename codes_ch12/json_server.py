# json_server.py

import socket

MAX_SIZE = 1024

host = socket.gethostname()
port = 12345
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(socket.gethostname())

s.bind((host, port))
s.listen(1)
conn, addr = s.accept()
print('Connected:', addr)

while True:
    data = conn.recv(MAX_SIZE)
    if not data:
        break
    conn.sendall(data)

conn.close()
