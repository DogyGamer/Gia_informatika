arr = open("./26.txt", "r").readlines()[1:]
arr = list(map(lambda x: int(x.replace("\n", "")), arr))

arr = sorted(arr, reverse=True)


prev = arr[0]
cntr = 1
for i in range(1,len(arr)):
    if prev-arr[i] >= 8:
        prev = arr[i]
        cntr += 1
        
print(cntr, prev)