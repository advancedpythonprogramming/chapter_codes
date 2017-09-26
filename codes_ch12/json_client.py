# json_client.py

import socket
import sys
import json

MAX_SIZE = 1024

server_host = socket.gethostname()
port = 12345
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Info to send as dictionary
info = {"name": "Johanna", "female": True}

# Create a string
message = json.dumps(info)

try:
    s.connect((server_host, port))

except socket.gaierror as err:
    print("Error: Connection error {}".format(err))
    sys.exit()

# Send a message as bytes
s.sendall(bytes(message, "UTF-8"))

# Wait for response, then we decode it and convert it to JSON
data = json.loads(s.recv(MAX_SIZE).decode('UTF-8'))
print(data)
s.close()
