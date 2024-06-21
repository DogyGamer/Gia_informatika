from math import floor

dp = [0]*(42**2)
dp[2] = 1

for i in range(3, 41):
    if i == 11 or i == 12:
        dp[i] = 0
        continue
    
    
    dp[i] += dp[i-1]
    
    prevx2 = i // 2
    if i % 2 == 0 and (prevx2 >= 10 or i <= 10):
        dp[i] += dp[prevx2]
        
    prevsqr2 = i**0.5
    iprevsq2 = floor(prevsqr2)
    if floor(prevsqr2) ** 2 == i and (iprevsq2 >= 10 or i <= 10):
        dp[i] += dp[iprevsq2]
        
print(dp[:42])
print(dp[40])