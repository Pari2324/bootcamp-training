# sum of prefix sum of an array
arr = [1,2,3,4,5]
for i in range(1, len(arr)):
    arr[i] = arr[i] + arr[i - 1]
print("prefix sum of array:", arr)