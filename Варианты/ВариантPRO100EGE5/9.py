lines = list(map(lambda x: list(map(int, x.replace("\n", "").split(";"))), open("./9_12918.csv", "r").readlines() ))

cntr = 0

min_ind = 9999_9999

for i in range(len(lines)):
    
    line = lines[i]
    if min(line)*max(line) <= sum(line)-(max(line)+min(line)):
        continue
    
    counts = {k:0 for k in set(line)}
    for x in line:
        counts[x] += 1
    
    if counts[max(line)] != 1:
        continue
    
    if len(set(line)) == 4 and len([x for x,c in counts.items() if c == 2]) == 2 and len([x for x,c in counts.items() if c == 1]) == 2:
        min_ind = min(min_ind, i)
        cntr += 1
        
print(cntr)
print(min_ind, sum(lines[min_ind]))