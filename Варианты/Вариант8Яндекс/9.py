lines = list(map(lambda x: list(map(int, x.replace("\n", "").split(";"))), open("./9(5).csv","r").readlines()))

for i in range(len(lines)):
    line = lines[i]
    cnts = {k:0 for k in set(line)}
    for a in line:
        cnts[a] += 1
    
    l2 = [k for k,v in cnts.items() if v == 2]
    
    l3 = [k for k,v in cnts.items() if v == 3]
    l1 = [k for k,v in cnts.items() if v == 1]
    
    if len(l2) == 1 and len(l3) == 1 and len(l1) == 3:
        if l3[0] > l2[0]:
            print(i, line)
        
3319
