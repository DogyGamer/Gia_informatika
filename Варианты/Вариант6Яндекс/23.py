dp = [0]*20
dp[3] = 1

for i in range(4, 17):
    
    dp[i] += dp[i-1]
    
    prevfrom2 = i // 2
    if i % 2 == 0 and (prevfrom2 >= 6 or i <= 6) and (prevfrom2 >= 12 or i <= 12):
        dp[i] += dp[prevfrom2]
        
        
print(dp)
print(dp[16])
    