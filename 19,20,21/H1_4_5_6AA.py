moves_left = [0]*(48*2)

def win_moves(S):
    res = [moves_left[S+1], moves_left[S+4], moves_left[S*2]]
    return [x for x in res if x % 2 == 0]

for S in range(46, 0, -1):
    wmv = win_moves(S)
    
    if len(wmv) == 0:
        moves_left[S] = max(moves_left[S+1], moves_left[S+4], moves_left[S*2]) + 1
    else:
        moves_left[S] = min(wmv) + 1
        
for i in range(len(moves_left)):
    print(i, moves_left[i], sep="\t")