# pickle.py

import socket
import sys
import pickle_

MAX_SIZE = 1024

server_host = socket.gethostname()
port = 12345
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


class Person:

    def __init__(self, name, male):
        self.name = name
        self.male = male


person = Person("Sarah", True)
message = pickle_.dumps(person)

try:
    s.connect((server_host, port))

except socket.gaierror as err:
    print("Error: Connection error {}".format(err))
    sys.exit()

s.sendall(message)
data = pickle_.loads(s.recv(MAX_SIZE))
print(data.name)
s.close()
