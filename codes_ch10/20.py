# 20.py

content = "Sorry but now, this file will have me."
file = open('example_file', 'w', encoding='ascii', errors='replace')
file.write(content)
file.close()
