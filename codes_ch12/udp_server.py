# udp_server.py

import socket

MAXSIZE = 2048

server_name = socket.gethostbyname('localhost')
server_port = 25000

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("", server_port))

while True:
    data, addr = s.recvfrom(MAXSIZE)
    print(data.decode('ascii'))
    response = "Response for {}".format(addr[0])
    s.sendto(response.encode('utf-8'), addr)
