#count vowels in a string
s = " PARINEETA KAPOOR"
vowels = "AEIOUaeiou"
count = 0
for ch in s:
    if ch in vowels:
        count += 1
print("Number of vowels in the string:", count)