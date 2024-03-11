# 27747

n = 83*4
dp = [[0]*n for _ in range(n)] 

def get_win_moves(i, j):
    moves = [dp[i+1][j], dp[i*4][j], dp[i][j+1], dp[i][j*4]]
    return [x for x in moves if x % 2 == 0]

for i in range(77, 0, -1):
    for j in range(77, 0, -1):
        if i+j >= 82:
            dp[i][j] == 0
            continue
        
        wmoves = get_win_moves(i, j)
        if len(wmoves) == 0:
            dp[i][j] = max([dp[i+1][j], dp[i*4][j], dp[i][j+1], dp[i][j*4]])+1
        else:
            dp[i][j] = min(wmoves) + 1
            
for i in range(1, 79):
    print(i, dp[4][i], sep="\t")

# 19 - 5+
# 20 - 1619+
# 21 - 18+
