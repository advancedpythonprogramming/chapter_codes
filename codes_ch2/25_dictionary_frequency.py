# A string to be verified and a empty dictionary to count vowels
msg = 'supercalifragilisticexpialidocious'
vowels = dict()

for v in msg:
    if v not in 'aeiou':  # check wheter v is vowel or not
        continue

    # If v exist, add a key named as v initialized at 0
    if v not in vowels:
        vowels[v] = 0

    # If v alread exist, increase the counter
    vowels[v] += 1

print(vowels)
