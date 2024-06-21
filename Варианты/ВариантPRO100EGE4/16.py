dp = [0,1,2]

for i in range(3, 40):
    if i % 2 == 0:
        a = dp[i-1]+ dp[i-2] + 1
    else:
        a = sum(dp[:i])
        
    dp.append(a)
    
print(dp)
print(dp[38])

# 6202126849