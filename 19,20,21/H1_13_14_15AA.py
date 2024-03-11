# 27754

n = 62*4
dp = [[0]*n for _ in range(n)]

def get_win_moves(i, j):
    moves = [dp[i+1][j], dp[i*4][j], dp[i][j+1], dp[i][j*4]]
    return [x for x in moves if x % 2 == 0]

for i in range(57, 0, -1):
    for j in range(57, 0, -1):
        if i+j >= 61:
            dp[i][j] = 0
            continue
        
        moves = get_win_moves(i, j)
        if len(moves) == 0:
            dp[i][j] = max([dp[i+1][j], dp[i*4][j], dp[i][j+1], dp[i][j*4]])+1
        else:
            dp[i][j] = min(moves) + 1
            
            
for i in range(1, 57+4):
    print(i, dp[3][i], sep="\t")
    
# 19 - 4+
# 20 - 1214+
# 21 - 14+
