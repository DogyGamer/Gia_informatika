dp = [[0]*(232*3) for _ in range(232*3)]

def gwmoves(i,j):
    moves = [dp[i+4][j], dp[i*3][j], dp[i][j+4], dp[i][j*3]]
    return [x for x in moves if x%2 == 0]

for i in range(217, 0, -1):
    for j in range(217, 0, -1):
        if i+j >= 231:
            dp[i][j] = 0
            continue
        
        wmoves = gwmoves(i, j)
        if len(wmoves) == 0:
            dp[i][j] = max(dp[i+4][j], dp[i*3][j], dp[i][j+4], dp[i][j*3]) +1 
        else:
            dp[i][j] = min(wmoves) + 1
            
for i in range(1, 218):
    if dp[10][i] == 4:
        print(i, dp[10][i], sep="\t")
        