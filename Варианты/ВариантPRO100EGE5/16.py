dp = [1,1]

for i in range(2,2030):
    dp.append(dp[i-1]*i)
    
print(dp[2024])
print(dp[2022])
print(dp[2024]/dp[2022])