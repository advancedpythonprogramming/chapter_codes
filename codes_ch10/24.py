# 24.py

num_lines = 100

file = open('example_file_3', 'wb')
for i in range(num_lines):
    # To the bytes function we should pass an iterable with the content to
    # convert. For this reason we pass the integer inside the list
    content = b"line_" + bytes([i]) + b" abcde12"
    file.write(content)
file.close()

file = open('example_file_3', 'rb')
# The number 40 indicates the number of bytes that will be read from the file
print(file.read(40))
file.close()
