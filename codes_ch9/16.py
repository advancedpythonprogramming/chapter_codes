# 16.py

characters = "estación"
print(characters.encode("ascii", errors='replace'))  
print(characters.encode("ascii", errors='ignore'))
print(characters.encode("ascii", errors='xmlcharrefreplace'))
