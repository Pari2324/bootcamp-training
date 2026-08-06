#convert upper case but without using upper() function use ASCII values
s = "python programming"
upper_s = ""
for ch in s:
    if 'a' <= ch <= 'z':
        upper_s += chr(ord(ch) - 32)
    else:
        upper_s += ch
print("String in upper case:", upper_s)