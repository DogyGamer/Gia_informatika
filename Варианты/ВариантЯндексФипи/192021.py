moves = [0]*(310*5)

def gwmvs(i):
    mvs = [moves[i+3], moves[i*5]]
    return mvs, [x for x in mvs if x % 2 == 0]


for i in range(300, 0,-1):
    mvs,wmvs = gwmvs(i)
    
    if len(wmvs) == 0:
        moves[i] = max(mvs) + 1
    else:
        moves[i] = min(wmvs) + 1
        
for i in range(1, 301):
    r = moves[i]
    if r == 3:
        print(i, r)
    