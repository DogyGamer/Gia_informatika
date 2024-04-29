arr = open("./17(3).txt", "r").readlines()
arr = list(map(lambda x: int(x.replace("\n", "")), arr))

mx = max([a for a in arr if len(str(a)) == 4]) ** 3

cntr = 0
mxsum = 0

for i in range(1, len(arr)-1):
    a = arr[i-1]
    b = arr[i]
    c = arr[i+1]
    
    de = [a,b,c]
    
    if sum([str(x)[-1] == "3" or str(x)[-1] == "5" for x in de]) > 1 and a*b*c <= mx:
        mxsum = max(mxsum, sum(de))
        cntr += 1
        
print(cntr, mxsum)
    