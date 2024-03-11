line = open("./24/H1/2.txt", 'r').readlines()[0].replace("\n", "")

start = 0
letters = {k:[] for k in "AEIOUY"}
disabled = "VXZ"

maxlen = 0

for i in range(len(line)):
    s = line[i]
    if s in disabled:
        maxlen = max(maxlen, i-start)
        start = i+1
        continue

    if s in letters.keys():
        letters[s].append(i)
        if len(letters[s]) > 8:
            start = letters[s].pop() + 1
            
    for s2 in letters.keys():
        letters[s2] = [x for x in letters[s2] if x > start]
                
    maxlen = max(maxlen, i-start)
print(maxlen)