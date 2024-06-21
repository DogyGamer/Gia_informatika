moves = [0]*(42*2)

def getwmoves(n):
    mvs = [moves[n+1], moves[n*2]]
    return [x for x in mvs if x % 2 == 0], mvs

for n in range(40,0, -1):
    if n >=21:
        moves[n] = 0
        continue
    wmvs, mvs = getwmoves(n)    
    if len(wmvs) == 0:
        moves[n] = max(mvs) + 1
    else:
        moves[n] = min(wmvs) + 1
        
for i in range(1,23):
    if moves[i] == 5:
        print(i, moves[i])