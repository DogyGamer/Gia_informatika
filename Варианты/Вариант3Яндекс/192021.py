moves = [[0]*(189*3) for _ in range(189*3)]

def getwmoves(i,j):
    ind = max(i,j)
    mvs = [moves[i+j][j], moves[i][j+i]]
    mvs.append(moves[ind][ind])
    return [x for x in mvs if x % 2 == 0], mvs


for i in range(189, 0, -1):
    for j in range(189, 0, -1):
        if i+j >= 189:
            moves[i][j] = 0
            continue
        
        wmvs, mvs = getwmoves(i,j)
        if len(wmvs) == 0:
            moves[i][j] = max(mvs) + 1
        else:
            moves[i][j] = min(wmvs) + 1
            
for i in range(1,190):
    r = moves[5][i]
    if r == 3:
        print(i, moves[5][i], sep="\t")
    
# 19 пересчитал на листке, получилось. А вот 20 и 21 не понимаю как исправить =(
    