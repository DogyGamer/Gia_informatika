dp = [0]*(45*3)

dp[7] = 1

for i in range(7, 45):
    if i == 11:
        dp[i] = 0
        continue
    
    prp1 = i-1
    prp4 = i-4
    prm3 = i // 3
    
    dp[i] += dp[prp1]
    if prp4 >= 27 or i <= 27:
        dp[i] += dp[prp4]
    
    if i % 3 == 0 and (prm3 >= 27 or i <= 27):
        dp[i] += dp[prm3]
        
print(dp)
print(dp[42])