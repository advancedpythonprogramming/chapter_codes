# fragmented.py

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
MAX_SIZE = 1024

fragments = []
finish = False
while not finish:
    chunk = s.recv(MAX_SIZE)
    if not chunk:
        break
    fragments.append(chunk)

# Joining original message
message = "".join(fragments)
