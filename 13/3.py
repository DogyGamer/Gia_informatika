from itertools import product

cntr = 0

for a in product([0,1], repeat=5):
    b = [0,1,1]
    b.extend(a)
    flag = True
    for i in range(1,7):
        if b[i-1] == b[i] and b[i+1] == b[i]:
            flag = False
        
    if flag:
        cntr +=1

print(cntr)
            