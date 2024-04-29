dp = [1]*2029


for i in range(2028, -1, -1):
    if i >= 2024:
        dp[i] = 1
    else:
        dp[i] = dp[i+4] + dp[i+2]
    
    
print(len(set(dp)))

# Похоже индексом ошибся внес условие if i >= 2024: и все получилось
