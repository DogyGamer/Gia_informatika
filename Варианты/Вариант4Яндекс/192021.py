moves = [[0]*(200*2) for _ in range(200*2)]

def getwmoves(i,j):
    wmvs = [moves[i+2][j], moves[i][j+2], moves[i+j][j], moves[i][i+j]]
    
    return [x for x in wmvs if x%2 == 0], wmvs


for i in range(180, 0, -1):
    for j in range(180, 0, -1):
        if i+j >= 180:
            moves[i][j] = 0
            continue
        
        wmvs, mvs = getwmoves(i,j)
        
        if len(wmvs) == 0:
            moves[i][j] = max(mvs) + 1
        else:
            moves[i][j] = min(wmvs) + 1
            
            
for i in range(180):
    if moves[18][i] == 4:
        print(i, moves[18][i])