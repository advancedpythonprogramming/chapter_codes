# 28.py

from io import StringIO, BytesIO

# Simulate a text file
file_in = StringIO("info, text and more")
# Simulate a binary blob file
file_out = BytesIO()

char = file_in.read(1)
while char:
    file_out.write(char.encode('ascii', 'ignore'))
    char = file_in.read(1)

buffer_ = file_out.getvalue()
print(buffer_)
