# 1. Create HashMap
m = {}

# 2. Add / Insert
m["a"] = 1
m["b"] = 2

print(m)
# {'a': 1, 'b': 2}


# 3. Access value
print(m["a"])
# 1


# 4. Update value
m["a"] = 10

print(m)
# {'a': 10, 'b': 2}


# 5. Check if KEY exists
if "a" in m:
    print("Found")


# 6. Check if KEY does NOT exist
if "c" not in m:
    print("Not Found")


# 7. Get value safely
print(m.get("a"))
# 10

print(m.get("c"))
# None

print(m.get("c", 0))
# 0


# 8. Count frequency - normal way
nums = [1, 2, 2, 3, 3, 3]

count = {}

for num in nums:
    if num in count:
        count[num] += 1
    else:
        count[num] = 1

print(count)
# {1: 1, 2: 2, 3: 3}


# 9. Count frequency - using get()
count = {}

for num in nums:
    count[num] = count.get(num, 0) + 1

print(count)
# {1: 1, 2: 2, 3: 3}


# 10. Loop through KEYS
for key in count:
    print(key)


# 11. Loop through VALUES
for value in count.values():
    print(value)


# 12. Loop through KEY + VALUE
for key, value in count.items():
    print(key, value)


# 13. Get all keys
print(count.keys())


# 14. Get all values
print(count.values())


# 15. Convert keys to list
print(list(count.keys()))


# 16. Convert values to list
print(list(count.values()))


# 17. Remove a key
del count[1]

print(count)


# 18. Remove safely
count.pop(2)

print(count)


# 19. Check length
print(len(count))


# 20. Clear HashMap
count.clear()

print(count)
# {}
