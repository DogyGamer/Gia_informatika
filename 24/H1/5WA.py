line = open("./24/H1/5.txt", "r").readlines()[0].replace("\n", "")

letters = {chr(k):[] for k in range(65,90+1)}

start = 0
lmax = 0

for i in range(1,len(line)):
    s = line[i]
    
    letters[s].append(i)
    if len(letters[s]) > 10:
        start = letters[s].pop() + 1
        
    for s2 in letters.keys():
        letters[s2] = [x for x in letters[s2] if x > start]
        
    lmax = max(lmax, i-start+1)
    
print(lmax)