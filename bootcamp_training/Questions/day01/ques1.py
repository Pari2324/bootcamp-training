#count even and odd number in an array
arr = [30,2,18,17,31,54]
even_count = 0
odd_count = 0
for i in arr:
    if i % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print("even count =", even_count)
print("odd count =", odd_count)
