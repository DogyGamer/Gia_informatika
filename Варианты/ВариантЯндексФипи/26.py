lines = open("./26(8).txt", "r").readlines()

N = int(lines[0])
lines = lines[1:]

d = []

for line in lines:
    s,e = list(map(int, line.split()))
    
    d.append([s, True])
    d.append([e, False])
    
print(sorted(d))
d = sorted(d)

cntr = 0
res = []
for t,isenter in d:
    if isenter:
        cntr += 1
    else:
        cntr -= 1
    res.append(cntr)
    
print(max(res), res.count(max(res)))