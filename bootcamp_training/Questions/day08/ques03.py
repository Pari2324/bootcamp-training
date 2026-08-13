# 21. Two Sum - HashMap
nums = [2, 7, 11, 15]
target = 9

m = {}

for i in range(len(nums)):

    needed = target - nums[i]

    if needed in m:
        print([m[needed], i])
        break

    m[nums[i]] = i


# 22. Frequency of characters
s = "anagram"

count = {}

for ch in s:
    count[ch] = count.get(ch, 0) + 1

print(count)


# 23. Check duplicate
nums = [1, 2, 3, 1]

seen = {}

for num in nums:

    if num in seen:
        print("Duplicate found")
        break

    seen[num] = 1


# 24. Intersection of two arrays
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]

m = {}

for num in nums1:

    if num in nums2:
        m[num] = 1

print(list(m.keys()))
# [2]


# 25. Find element frequency
nums = [1, 2, 2, 3, 3, 3]

count = {}

for num in nums:
    count[num] = count.get(num, 0) + 1

print(count[3])
# 3


# 26. Find first unique character
s = "leetcode"

count = {}

for ch in s:
    count[ch] = count.get(ch, 0) + 1

for i in range(len(s)):

    if count[s[i]] == 1:
        print(i)
        break


# 27. Find most frequent element
nums = [1, 2, 2, 3, 3, 3]

count = {}

for num in nums:
    count[num] = count.get(num, 0) + 1

max_count = 0
answer = None

for num in count:

    if count[num] > max_count:
        max_count = count[num]
        answer = num

print(answer)
# 3


# 28. Group elements
nums = [1, 2, 1, 3, 2]

groups = {}

for num in nums:

    if num not in groups:
        groups[num] = []

    groups[num].append(num)

print(groups)


# 29. Dictionary with list
m = {}

m[1] = []
m[1].append("apple")
m[1].append("banana")

print(m)
# {1: ['apple', 'banana']}


# 30. Dictionary with set
m = {}

m[1] = set()

m[1].add("apple")
m[1].add("apple")
m[1].add("banana")

print(m)
# {1: {'apple', 'banana'}}