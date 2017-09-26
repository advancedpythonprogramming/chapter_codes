# 22.py

content = "\nI will be added to the end."
file = open('example_file', 'a', encoding='ascii', errors='replace')
file.write(content)
file.close()

file = open('example_file', 'r', encoding='ascii', errors='replace')
print(file.read())
file.close()
