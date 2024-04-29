dp = [0]*10000000

dp[1] = 2

for n in range(2, 10000000):
    if n > 1 and dp[n-1] < 7555444:
        dp[n] = dp[n-1]+6
    else:
        dp[n] = dp[n-1] - 7555444
        
print(max(dp))