#37154
moves = [0]*(40*2)

def getwinmoves(S):
    wmoves = [moves[S+1], moves[S+4], moves[S*2]]
    return [x for x in wmoves if x % 2 ==0]

for S in range(39,0,-1):
    wmoves = getwinmoves(S)
    
    if len(wmoves) == 0:
        moves[S] = max(moves[S+1], moves[S+4], moves[S*2]) + 1
    else:
        moves[S] = min(wmoves) + 1
        
for i in range(1, 42):
    print(i, moves[i], sep="\t")