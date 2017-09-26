# 18.py

print(ord(b"a"))
b = bytearray(b'abcdef')
b[3] = ord(b'g')  # The ASCII code for g is 103
b[4] = 68  # The ASCII code for D is 68, this is the same as b[4] = ord(b'D')
print(b)
