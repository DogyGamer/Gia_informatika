dp = [0]*60
dp[58] = 1

for i in range(58, 2, -1):
    nextfrom_del = i // 3
    next_min = i - (i % 3)
    if (i % 3) == 0:
        next_min = i-1
    
    dp[next_min] += dp[i]
    dp[nextfrom_del] += dp[i]
    
print(dp)
print(dp[3]) 
