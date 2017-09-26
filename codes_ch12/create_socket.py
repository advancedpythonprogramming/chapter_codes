# create_socket.py

import socket

# Create TCP IPv4 socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(s)
