lines = list(map(lambda x: int(x.replace("\n", "")),open("./17(5).txt", "r").readlines()))

maxc21 = max([x for x in lines if x % 21 == 0])

cntr = 0
minc = 999_999_999

for i in range(1, len(lines)):
    a = lines[i]
    b = lines[i-1]
    
    if a > maxc21 or b > maxc21:
        cntr += 1
        minc = min(minc, a+b)
        
print(cntr, minc)