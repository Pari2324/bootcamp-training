#count zeroes in sorted binary error
arr=[1,1,1,1,1,1,1,1,0,0,0]
count=0
for i in arr:
    if i==0:
        count+=1
print("Number of zeroes:", count)
