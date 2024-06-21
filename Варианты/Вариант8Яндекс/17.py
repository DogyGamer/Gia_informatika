lines = list(map(int, open("./17(7).txt", "r").readlines()))

maxc = max([x for x in lines if x > 0 and len(str(x)) == 5 and str(x)[len(str(x))-2:] == "17"])

minf = float("inf")

cntr = 0

for i in range(len(lines)-2):
    arr = lines[i:i+3]
    
    if sum(list(map(abs, arr))) > maxc:
        continue

    if any(str(x)[len(str(x))-2:] == "17" for x in arr):
        cntr += 1
        minf = min(minf, sum(arr))
    
    
print(cntr, minf)