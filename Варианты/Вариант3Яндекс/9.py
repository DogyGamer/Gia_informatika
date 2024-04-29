lines = open("./Вариант3Яндекс/9.csv", "r").readlines()

cntr = 0

for line in lines:
    arr = list(map(int, line.replace("\n", "").split(";")))
    
    mx = max(arr)
    mxc = arr.count(mx)
    mi = min(arr)
    mic = arr.count(mi)
    
    if (len(arr)-mic-mxc) == 0:
        continue
    
    res = (sum(arr) - mi*mic - mx*mxc) / (len(arr)-mic-mxc)
    if res >= 8:
        cntr += 1
        
print(cntr)

# 2182
# 2065

# У меня было несколько вариантов, нужно ли отбрасывать все максимальные и минимальные оценки или только оду из них
# В случае если таких несколько. Как оказалось тут требуют делать по тупому мда.