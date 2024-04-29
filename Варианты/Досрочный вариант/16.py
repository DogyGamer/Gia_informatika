dp = [0]*2030

for i in range(2025):
    if i < 7:
        dp[i] = 1
    else:
        dp[i] = i+2+dp[i-1]
        
print(dp[2024]-dp[2020])