b'estaci\xc3\xb3n'
b'estaci\xf3n'
b'estaci\xa2n'

---------------------------------------------------------------------------
UnicodeEncodeError                        Traceback (most recent call last)
<ipython-input-32-844dd5b7b18c> in <module>()
      3 print(characters.encode("latin-1"))
      4 print(characters.encode("CP437"))
----> 5 print(characters.encode("ascii")) # can't enconde in ascii the character ó

UnicodeEncodeError: 'ascii' codec can't encode character '\xf3' in position 6: 
ordinal not in range(128)
