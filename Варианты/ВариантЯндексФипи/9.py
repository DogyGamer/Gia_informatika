lines = list(map(lambda x: list(map(int, x.replace("\n", "").split(";"))) ,open("./9(6).csv", "r").readlines()))

from itertools import permutations

cntr = 0

for line in lines:
    if not (max(line) < sum(line) - max(line)):
        continue
    
    if any([a1+a2 == a3+a4 for a1,a2,a3,a4 in permutations(line)]):
        cntr += 1
        
print(cntr)