dp = []

for n in range(20025):
    if n <= 1000:
        dp.append(f"(@{n}@)")
    else:
        if n > 1002 and n % 2 != 0:
            dp.append("!")
        else:
            dp.append(f"{n} + 2*({dp[n-2]}) + 6*({dp[n-6]})")
        
print(dp[20024])
# print(dp[1009])

# from sys import setrecursionlimit
# from functools import lru_cache
# setrecursionlimit(25_000)

# @lru_cache()
# def F(n):
#     if n <= 1000:
#         print(n)
#         return n**(n**2)
#     else:
#         print(n)
#         return n + 2*F(n-2) + 6*F(n-6)

# print(F(999), F(995))

# # print(F(1001))
# # print(F(1002))
# # print(F(1003))
# # print(F(1004))