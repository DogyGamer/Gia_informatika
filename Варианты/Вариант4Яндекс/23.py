dp = [0]*(130)
dp[2] = 1

from math import floor

for i in range(3, 129):
    # if i == 20:
    #     dp[i] = 0
    #     continue
    
    dp[i] += dp[i-3]
    
    if i % 2 == 0:
        prevfrom = i // 2
        # if prevfrom >= 12 or i <= 12:
        dp[i] += dp[i//2]
        
    if floor((i**0.5))**2 == i:
        prevfrom = int(i**0.5)
        # if prevfrom >= 12 or i <= 12:
        dp[i] += dp[int(i**0.5)]
print(dp)
print(dp[128])

# 368 - 1 усл
# 234 - 2 усл
# 156 - оба условия
# 576 - без усл
# 328 - оба условия не выполняются


# 368- правильный
