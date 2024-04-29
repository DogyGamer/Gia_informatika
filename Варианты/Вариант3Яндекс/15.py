

dp = [0]*2031
for i in range(2024, 2031):
    dp[i] = 1

def f(n):
    dp[n] = dp[n+2] + dp[n+4]

for i in range(2024, -1, -1):
    f(i)
    
print(len(set(dp)))