line = open("./24/H1/3.txt", 'r').readlines()[0].replace("\n", "")

letters = {k:[] for k in "XYZ"}

disabled = "ABC"
start = 0
lmax = 0

for i in range(1,len(line)):
    s = line[i]
    if s in disabled:
        if all([len(x) == 5 for x in letters.values()]):
            lmax = max(lmax, i-1-start)
        start = i+1
        continue
    
    if s in letters.keys():
        letters[s].append(i)
        if len(letters[s]) > 5:
            # for _ in range(len(letters[s])):
            start = letters[s].pop()+1
        
    for s2 in letters.keys():
        letters[s2] = [x for x in letters[s2] if x > start]
    
    if all([len(x) == 5 for x in letters.values()]):
        lmax = max(lmax, i-start)
            
print(lmax)