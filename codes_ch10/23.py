# 23.py

content = b"abcde12"
file = open('example_file_2', 'wb')
file.write(content)
file.close()

file = open('example_file_2', 'rb')
print(file.read())
file.close()
