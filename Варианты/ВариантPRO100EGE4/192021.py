moves = [0]*(135*2)

def getwmoves(i):
    wmvs = [moves[i+1], moves[i*2]]
    return wmvs, [x for x in wmvs if x % 2 == 0]


for i in range(129, 0,-1):
    mvs, wmvs = getwmoves(i)
    if len(wmvs) == 0:
        moves[i] = min(mvs) + 1
    else:
        moves[i] = max(wmvs) + 1
        
for i in range(1, 129):
    r = moves[i]
    if r == 5:
        print(i, r)