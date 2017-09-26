from collections import deque


class Word:

    def __init__(self, word=None):
        self.word = word
        self.characters = deque(self.word)

    def is_palindrome(self):
        if len(self.characters) > 1:
            return self.characters.popleft() == self.characters.pop() \
             and Word(''.join(self.characters)).is_palindrome()
        else:
            return True

p1 = Word("radar")
p2 = Word("level")
p3 = Word("structure")

print(p1.is_palindrome())
print(p2.is_palindrome())
print(p3.is_palindrome())