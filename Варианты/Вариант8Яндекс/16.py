dp = [1,1]

for i in range(2, 2026):
    
    if i % 2 == 0:
        dp.append(int((i/2))*dp[i-1])
    else:
        dp.append(int(((i-1)/2))*dp[i-1])
        
print(dp)
print((dp[2024]-dp[2022])/ dp[2021])