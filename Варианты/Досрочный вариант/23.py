dp = [0]*30
dp[4] = 1

for i in range(5, 16):
    dp[i] += dp[i-1]
    
    from2 = i // 2
    
    if (i % 2 == 0) and (from2 >= 8 or i <= 8) and (from2 >= 10 or i <= 10):
        dp[i] += dp[from2]
        
    
print(dp)
print(dp[15])
# 2