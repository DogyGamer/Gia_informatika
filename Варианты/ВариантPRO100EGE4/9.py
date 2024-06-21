lines = list(map(lambda x: list(map(int, x.replace("\n", "").replace("\t", " ").split())), open("./9_12463.txt", "r").readlines()))

cntr = 0

for line in lines:
    counts = {k:0 for k in set(line)}
    for x in line:
        counts[x] += 1
        
    c4 = len([k for k,v in counts.items() if v == 4 ]) == 1
    c2 = len([k for k,v in counts.items() if v == 2 ]) == 1
    c1 = len([k for k,v in counts.items() if v == 1 ]) == 3
    
    if not(c4 and c2 and c1):
        continue
    
    if sum([k for k,v in counts.items() if v == 1 ]) / 3 >= max([k for k,v in counts.items() if v >= 2 ]):
        cntr += 1
        
print(cntr)