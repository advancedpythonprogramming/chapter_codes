# 12.py

# What is between quotes is a byte object
characters = b'\x63\x6c\x69\x63\x68\xe9'
print(characters)
print(characters.decode("latin-1"))

# 61 and 62 are the hexadecimal representation of 'a' and 'b'
characters = b"\x61\x62"
print(characters.decode("ascii"))

# 97 and 98 are the corresponding ASCII code of 'a' and 'b'
characters = b"ab"
print(characters)
characters = bytes((97, 98))
print(characters)
print(characters.decode("ascii"))
