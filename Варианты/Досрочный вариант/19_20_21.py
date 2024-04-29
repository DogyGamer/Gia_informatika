moves = [[0]*123*3 for _ in range(123*3)]

def gwmvs(i,j):
    mvs = [moves[i+1][j],moves[i*2][j], moves[i][j+1], moves[i][j*2]]
    return [x for x in mvs if x % 2 == 0], mvs

for i in range(123, 0,-1):
    for j in range(123,0,-1):
        if i+j >= 123:
            moves[i][j] = 0
            continue
        
        wmvs, mvs = gwmvs(i,j)
        if len(wmvs) == 0:
            moves[i][j] = max(mvs)+1
        else:
            moves[i][j] = min(wmvs)+1
            
for i in range(110):
    if moves[13][i] == 4:
        print(i, moves[13][i], sep="\t")