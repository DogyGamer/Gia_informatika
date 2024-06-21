moves = [[0]*1007 for _ in range(1007)]

def gwmvs(i,j):
    mvs = [moves[i+3][j], moves[i*2][j], moves[i][j+3], moves[i][j*2]] 
    return mvs, [x for x in mvs if x % 2 == 0]

for i in range(503, 0, -1):
    for j in range(503,0, -1):
        if i + j >= 503:
            moves[i][j] = 0
            continue
        
        mvs, wmvs = gwmvs(i,j)
        if len(wmvs) == 0:
            moves[i][j] = max(mvs) + 1
        else:
            moves[i][j] = min(wmvs) + 1
            

for i in range(1, 488):
    r = moves[i][15]
    if r == 4:
        print(i, r)
        