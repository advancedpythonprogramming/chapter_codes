# tcp_server-listener.py

import socket

MAX_SIZE = 1024

s_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get local machine name
host = socket.gethostname()
port = 10001

s_client.connect((host, port))
data = s_client.recv(MAX_SIZE)
print(data.decode('ascii'))
s_client.close()
