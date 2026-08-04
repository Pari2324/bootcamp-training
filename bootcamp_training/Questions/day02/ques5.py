#suffix sum of an array
arr = [1,2,3,4,5]
for i in range(len(arr) -2, -1, -1):
    arr[i] = arr[i] + arr[i + 1]
print("suffix sum of an array:",arr)