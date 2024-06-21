from itertools import permutations
lines = list(map(lambda x: list(map(int, x.replace("\n", "").split(";"))), open("./9(4).csv", "r").readlines()))
# print(lines)

cntr = 0

for line in lines:
    if not any([a+b == c+d for a,b,c,d in permutations(line)]):
        continue
    
    if not(max(line) < sum(line)-max(line)):
        continue
    
    if sum(line) % 2 == 0:
        cntr += 1
        
print(cntr)