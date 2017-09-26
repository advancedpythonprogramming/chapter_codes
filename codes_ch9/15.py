# 15.py

characters = "estación"
print(characters.encode("UTF-8"))  # 8-bit Unicode Transformation Format
print(characters.encode("latin-1"))
print(characters.encode("CP437"))
print(characters.encode("ascii"))  # Can't enconde in ascii the character ó
