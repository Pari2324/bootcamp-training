#replace every vowel with * in a string
s = "PROGRAMMING"
vowels = "AEIOUaeiou"
for ch in s:
    if ch in vowels:
        s = s.replace(ch, "*")
print("String after replacing vowels with *:", s)