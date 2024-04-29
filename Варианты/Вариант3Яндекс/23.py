dp = [0]*200
dp[32] = 1

for i in range(31, -1, -1):
    prev1 = int(str(i)[0])**2
    # prev1 = int(str(i)[-1])**2
    # prev1 = int(str(i**2)[0])
    # prev1 = int(str(i**2)[-1])
    prev2 = sum(list(map(int, str(i))))
    
    dp[i] = dp[i+prev1] + dp[i+prev2]
    
print(dp)
print(dp[1])

# Я не понимаю что они подразумевают под первой цифрой в квадрате, но ни один из вариантов не подходит
