# udp_client.py

import socket

MAXSIZE = 2048

# Create connection
server_name = socket.gethostbyname('localhost')
server_port = 25000
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Create message
message = "Hi, I'm sending this message."
target = (server_name, server_port)

# Send message
s.sendto(message.encode('ascii'), target)

# Optionally, we can get back sent information
# Also we can get the sender address
data, address = s.recvfrom(MAXSIZE)
print(data.decode('utf-8'))
