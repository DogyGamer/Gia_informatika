# 27416
n = 79*2
dp = [[0]*n for _ in range(n)]

def getwmoves(i, j):
    moves = [dp[i+1][j], dp[i*2][j], dp[i][j+1], dp[i][j*2]]    
    return [x for x in moves if x % 2 == 0]

for i in range(78, 0, -1):
    for j in range(78, 0, -1):
        if(i+j) >= 77:
            dp[i][j] = 0
            continue
            
        wmoves = getwmoves(i, j)
        if len(wmoves) == 0:
            dp[i][j] = max([dp[i+1][j], dp[i*2][j], dp[i][j+1], dp[i][j*2]]) + 1
        else:
            dp[i][j] = min(wmoves) + 1

for i in range(1, 74):
    print(i, dp[7][i], sep="\t")
    
# 19 - 18+ 
# 20 - 3134+
# 21 - 30+