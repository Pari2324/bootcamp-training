# left rotate an array
arr = [1,2,3,4,5] 
temp = arr[0]
for i in range (0, len(arr)- 1):
    arr[i] = arr[i+1]
arr[len(arr)-1] = temp
print("Array after left rotation:", arr)
