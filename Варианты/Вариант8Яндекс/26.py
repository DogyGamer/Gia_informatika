lines = open("./26(7).txt", "r").readlines()

n, k = list(map(int, lines[0].split()))

lines = list(map(int, lines[1:]))

arr = []

for i in range(len(lines)):
    line = lines[i]
    arr.append([line, True, i])
    arr.append([line+60, False, i])
    
    
arr.sort()

in_work = {}

cntr = 0

for t, is_start, id in arr:
    if len(in_work.keys()) < 1 and is_start:
        in_work[id] = 2
        cntr += 1
        
    if not is_start and id in in_work.keys():
        del in_work[id]
        

print(cntr)
