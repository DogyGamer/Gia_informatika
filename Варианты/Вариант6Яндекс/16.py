dp = [0]*2100

for i in range(13):
    dp[i] = 1
    
for i in range(13, 2050):
    dp[i] = dp[i-1] + i - 2
    
    
print(dp[2024])
print(dp[2020])
print(dp[2024] - dp[2020])