# tcp_client.py

import socket
import sys

MAX_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect to a specify address
    s.connect(("www.python.org", 80))

    # Send a encoded string asking for the content of the page.
    # Check https://www.w3.org/Protocols/rfc2616/rfc2616-sec14
    #.html#sec14.23
    # for possible protocol updates.
    s.sendall("GET / HTTP/1.1\r\nHost: www.python.org\r\n\r\n"
              .encode('ascii'))

    # Receive the response. The argument indicates the buffer
    #size
    data = s.recv(MAX_SIZE)

    # Print received data after decoding
    print(data.decode('ascii'))

except socket.error:
    print("Connection error", socket.error)
    sys.exit()

finally:
    # Close connection
    s.close()
