# selection sorting
nums = [3, 5, 1, 2, 9]
n = len(nums)
for i in range(n):
    min_index = i
    for j in range(i+1, n):
        if nums[j] < nums[min_index]:
            min_index = j
    nums[i], nums[min_index] = nums[min_index], nums[i]
print(nums)