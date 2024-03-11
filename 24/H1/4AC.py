line = open("./24/H1/4.txt", "r").readlines()[0].replace("\n", "")

letters = {k:[] for k in "XY"}

banned = "A"
start = 0
lmax = 0

for i in range(len(line)):
    s = line[i]
    
    if s in banned:
        if all([len(x)==1 for x in letters.values()]):
            lmax = max(lmax, i-1-start)
        start = i+1
        continue
    
    if s in letters.keys():
        letters[s].append(i)
        if len(letters[s]) > 1:
            start = letters[s].pop() + 1
            
    for s2 in letters.keys():
        letters[s2] = [x for x in letters[s2] if x > start]

    if all([len(x)==1 for x in letters.values()]):
        lmax = max(lmax, i-start+1)
        
print(lmax)

# Странно индексы работают, теряюсь че включается а что нет
# В конце это i-start+1
