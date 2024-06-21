dp = [0]*2100

dp[0] = 1
dp[1] = 1

for n in range(2, 2051):
    if n % 2 ==0:
        dp[n] = dp[n-1] / 3
    else:
        dp[n] = dp[n-1] * 6
        
print(dp[2049], dp[2046])
print(dp[2049]/dp[2046])