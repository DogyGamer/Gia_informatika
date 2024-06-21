lines = list(map(int, open("./17(6).txt", "r").readlines()))

third_by_val = sorted(lines)[-3]

mxs = 0
cntr = 0

for i in range(len(lines)-2):
    arr = lines[i:i+3]
    
    if not (len([x for x in arr if x % 2 == 0]) <= 2):
        continue
    
    if sum(arr) <= third_by_val:
        cntr += 1
        mxs = max(mxs, sum(arr))
        
print(cntr, mxs)