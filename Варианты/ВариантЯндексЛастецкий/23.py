dp = [0]*120
dp[8] = 1

from math import floor

for i in range(9, 116):
    if i == 33:
        continue
    
    pp1 = i - 1
    pm2 = i // 2
    ps2 = int(i ** 0.5)
    
    dp[i] += dp[pp1]
    # 32
    if i % 2 == 0 and (pm2 >= 32 or i <= 32):
        dp[i] += dp[pm2]
    
    if floor(i**0.5)**2 == i and (ps2 >= 32 or i <= 32):
        dp[i] += dp[ps2]
        
        
for i in range(8, 116):
    print(i, dp[i], sep="\t")
# print(dp)
print(dp[115])
    
    

