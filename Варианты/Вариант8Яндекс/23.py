dp = [0]*45

dp[2] = 1

from math import floor as f

for i in range(3, 43):
    if i == 16:
        dp[i] = 0 
        continue
    
    pf2 = i - 2
    pf3 = i - 3
    pfsqr = int(i ** 0.5)
    
    if pf2 >= 25 or i <= 25:
        dp[i] += dp[pf2]
        
    if pf3 >= 25 or i <= 25:
        dp[i] += dp[pf3]
        
    if (f(i**0.5)**2 == i) and (pfsqr >= 25 or i <= 25):
        dp[i] += dp[pfsqr]


print(dp)
print(dp[42])