dp = [0]*2228
for i in range(2227, 0, -1):
    if i >= 2025:
        dp[i] = i
    else:
        dp[i] = dp[i+3] + 3 + i
print(dp[23]-dp[21])