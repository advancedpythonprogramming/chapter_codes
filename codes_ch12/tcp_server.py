# tcp_server.py

import socket

# Create a TCP IPv4 socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 10001

# Bind the socker to the host and port
s.bind((host, port))

# We ask the operating system to start listening connections through
# the socket.
# The argument correspond to the maximun allowed connections.
s.listen(5)

count = 0
while True:
    # Stablish connection
    s_client, address = s.accept()
    print("Connection from:", address)

    # Prepare message
    message = "{}. Hi new friend!\n".format(count)

    # Change encoding and send
    s_client.send(message.encode("ascii"))

    # Clonse current connection
    s_client.close()
    count += 1
