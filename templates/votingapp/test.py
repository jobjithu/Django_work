arr = [2,4,5,2,6,8,5,4,6,7,9,3,4,6,7,5,4,3,5,7,2]

mydict = dict()

for key in arr:
    if key not in mydict:
        mydict[key] = 1
    else:
        mydict[key]+=1
print(arr)
arr.sort()
print(*arr)
print(mydict)            