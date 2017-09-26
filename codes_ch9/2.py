# isalpha() returns True if all the characters in the string are in the
# alphabet of some language. If there is a number, blank space or
# punctuation marks in the string, it will return False
print("abn".isalpha())

print("t/".isalpha())

# isdigit() returns True if all the characters in the string are digits
print("34".isdigit())

s = "I'm programming"
print(s.startswith("I'm"))
print(s.endswith("ing"))

# find(seq) returns the index of s where the argument's sequence seq starts
print(s.find("m p"))

# str.index(str, beg=0 end=len(string)-1) returns the index of s where the
# argument's sequence 'str' starts. It only searches in the substring
# that starts at position 4 and ends at position 10
print(s.index('o', 4, 10))

# If you do not explicit the beginning or ending of the substring, Python
# will use by default beg=0 and end=len(string)-1. It will return the
# first apparition of the argument's sequence in the string s
print(s.index('g'))

# Python will let you know if you fail your search
print(s.index('i', 5, 10))

# Generate a list of words in s separated by blank spaces
s = "Hi everyone, how are you?"
s2 = s.split()
print(s2)

# Create a string by concatenating the words in s2 using the # character
s3 = '#'.join(s2)
print(s3)

print(s.replace(' ', '**'))
print(s)

s5 = s.partition(' ')
print(s5)
print(s)
