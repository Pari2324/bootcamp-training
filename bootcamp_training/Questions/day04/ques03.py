#count digits in a string
s = "A1B2C3D478674769SDJFGHUYGTE"
d = "0123456789"
count = 0
for ch in s:
    if ch in d:
        count += 1
print("Number of digits in the string:", count)