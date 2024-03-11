lines = open("./27/H1_11_B.txt", "r").readlines()[1:]

sum_big = 0
sum_small = 0

min_diff_big_0_sm_1 = 999_999_999
min_diff_big_1_sm_0 = 999_999_999
min_diff_big_1_sm_1 = 999_999_999

for line in lines:
    a,b = list(map(int, line.split()))

    if a % 2 == 0:
        continue
    
    big = max(a,b)
    small = min(a,b)
    
    if big % 2 == 0 and small % 2 == 1:
        min_diff_big_0_sm_1 = min(min_diff_big_0_sm_1, big+small)
    elif big % 2 == 1 and small % 2 ==0:
        min_diff_big_1_sm_0 = min(min_diff_big_1_sm_0, big+small)    
    elif big % 2 == 1 and small % 2 ==1:
        min_diff_big_1_sm_1 = min(min_diff_big_1_sm_1, big+small)
        
    sum_big += big
    sum_small += small

S = sum_big + sum_small

# big - 1           small - 0

if sum_big % 2 == 0 and sum_small % 2 == 0:
    S -= min(min_diff_big_1_sm_0, min_diff_big_1_sm_1+min_diff_big_0_sm_1)
elif sum_big % 2 == 0 and sum_small % 2 == 1:
    S -= min(min_diff_big_1_sm_1, min_diff_big_1_sm_0+min_diff_big_0_sm_1)
# elif sum_big % 2 == 1 and sum_small % 2 == 0:
#     pass
elif sum_big % 2 == 1 and sum_small % 2 == 1:
    S -= min(min_diff_big_0_sm_1, min_diff_big_1_sm_1+min_diff_big_1_sm_0)
    
print(S)

# 44067 - OK

# 301653067 - OK
# 301653067