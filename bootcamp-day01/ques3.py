#find floor and ceil values of a number without using functions
nums=int(input("Enter a number ="))
arr=[10,7,3,12,15]
floor=-1
ceil=-1
for i in arr:
    if i < nums:
        floor = max(floor, i)
    elif i > nums:
        ceil = min(ceil, i) if ceil != -1 else i

print("Floor value:", floor)
print("Ceil value:", ceil)