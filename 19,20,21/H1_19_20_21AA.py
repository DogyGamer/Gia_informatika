moves = [0]*(29*2) 

def getwinmoves(S):
    return [x for x in [moves[S+1], moves[S*2]] if x % 2 == 0]

for S in range(28,0,-1):
    wmoves = getwinmoves(S)
    if len(wmoves) == 0:
        moves[S] = max([moves[S+1], moves[S*2]]) + 1
    else:
        moves[S] = min(wmoves) + 1
        
for i in range(1, 30, 1):
    print(i, moves[i], sep="\t")