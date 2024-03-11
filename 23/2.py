dp = [0 for i in range(0, 45) ]

dp[2] = 1
for i in range(3, 45):
    
    if i == 29:
        continue
    
    prev_from_3 = i//3
    prev_from_2 = i //2 
    if (i % 3 == 0 and ((i <= 13) or prev_from_3 >= 13 )):
        dp[i] += dp[prev_from_3]
    if(i % 2 == 0 and ((i <= 13) or prev_from_2 >= 13 )):
        dp[i] += dp[prev_from_2]
    
    dp[i] += dp[i-1]
    
print(dp)
print(dp[44])