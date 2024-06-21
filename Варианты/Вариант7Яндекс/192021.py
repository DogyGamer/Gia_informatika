moves = [[0]*(150*3) for _ in range(150*3)]

def getwmoves(i,j):
    mvs = [moves[i+2][j], moves[i*3][j], moves[i][j+2], moves[i][j*3]]
    
    return [x for x in mvs if x % 2 == 0], mvs 


for i in range(150, 0, -1):
    for j in range(150, 0, -1):
        if i+j >= 150:
            moves[i][j] = 0
            continue
        
        wmvs, mvs = getwmoves(i,j)
        if len(wmvs) == 0:
            moves[i][j] = max(mvs) + 1
        else:
            moves[i][j] = min(wmvs) + 1
        

for i in range(1,134):
    if moves[i][16] == 4:
        print(i, moves[i][16])
