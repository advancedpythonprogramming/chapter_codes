# 17.py

ba_1 = bytearray(b"hello world")
print(ba_1)
print(ba_1[3:7])
ba_1[4:6] = b"\x15\xa3"
print(ba_1)
ba_1.extend(b"program")
print(ba_1)
# Here it prints an int, the ascii that corresponds to the letter 'h'
print(ba_1[0])
print(bin(ba_1[0]))
print(bin(ba_1[0])[2:].zfill(8))
