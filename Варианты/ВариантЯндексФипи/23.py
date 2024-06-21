dp = [0]*110
dp[1] = 1

for i in range(2, 53):
    
    pp2 = i-2
    pm2 = i // 2
    
    if pp2 >= 18 or i <= 18:
        dp[i] += dp[pp2]
        
    if i%2==0 and (pm2 >= 18 or i <= 18):
        dp[i] += dp[pm2]
            

for i in range(1, 53):
    print(i, dp[i])
print(dp[52])