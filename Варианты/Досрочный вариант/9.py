lines = open("./9.csv", "r").readlines()

from itertools import permutations

cntr = 0

for line in lines:
    line = list(map(lambda x: int(x.replace("\n", "")), line.split(";")))
    
    if not (max(line) < (sum(line)-max(line))):
        continue
    
    if any([p[0]+p[1] == p[2]+p[3] for p in permutations(line)]):
        cntr += 1
        
print(cntr)