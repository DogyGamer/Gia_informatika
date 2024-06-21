dp = [1,1]

for n in range(2,60):
    if n % 3 == 0:
        a = dp[n-1] + (n // 3)
    else:
        a = dp[n-1] + dp[n-2]
    
    dp.append(a)
    
print(dp[54] - dp[52] - dp[50])