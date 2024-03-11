lines = open("./24/24_5.txt", "r").readlines()

lmax = 0

for line in lines:
    dicti = {chr(x):[] for x in range(65, 91)}
    a_cntr = 0
    line = line.replace("\n", "")
    for i in range(len(line)):
        letter = line[i]
        if letter == "A":
            a_cntr += 1
        
        dicti[letter].append(i)
        
    if a_cntr < 25:
        lmax = max(lmax, max([x[-1]-x[0] for x in dicti.values() if len(x) >= 2]))
        
print(lmax)