#extract all digits from a string
s = "abc123xy2456"
digits = " "
for ch in s:
    if ch.isdigit():
        digits += ch
print("Digits in the string:", digits)