lines = open("./27/H1_9_B.txt", "r").readlines()[1:]


S = 0
n_chet = 0
n_nechet = 0

mind_diff_nechet = 999_999_999
mind_diff_nechet_2 = 999_999_999

mind_diff_chet = 999_999_999
mind_diff_chet_2 = 999_999_999

for line in lines:
    a,b = list(map(int, line.split()))
    
    c = max(a,b)
    if c % 2 == 0:
        n_chet += 1
    else:
        n_nechet += 1
        
    diff = max(a,b) - min(a,b)    

    if a % 2 != b % 2:
        if c % 2 == 0:
            if mind_diff_chet > diff:
                mind_diff_chet_2 = mind_diff_chet
                mind_diff_chet = diff
            elif mind_diff_chet_2 > diff:
                mind_diff_chet_2 = diff
            # mind_diff_chet = min(mind_diff_chet, max(a,b) - min(a,b))
        else:
            if mind_diff_nechet > diff:
                mind_diff_nechet_2 = mind_diff_nechet_2
                mind_diff_nechet = diff
            elif mind_diff_nechet_2 > diff:
                mind_diff_nechet_2 = diff
            # mind_diff_nechet = min(mind_diff_nechet, max(a,b) - min(a,b))
    S += c
    
if n_chet - n_nechet > 1:
    if S %2 != 0:
        S -= min(mind_diff_chet, mind_diff_nechet)
elif n_nechet - n_chet > 1:
    if S % 2 == 0:
        S -= min(mind_diff_chet, mind_diff_nechet)
elif n_chet > n_nechet:
    if S % 2 != 0:
        S -= min(mind_diff_nechet, mind_diff_chet+mind_diff_chet_2)
else:
    if S % 2 == 0:
        S -= min(mind_diff_chet, mind_diff_nechet+mind_diff_nechet_2)
    

    
# if n_chet > n_nechet:
#     if S % 2 != 0:
#         S -= mind_diff
# else:
#     if S % 2 == 0:
#         S -= mind_diff
        
print(n_chet, n_nechet, S % 2 == 0)
print(S)

# Нипон, первое сошлось, второе чуть-чуть отличается
# 36898631
# 36898658 - OK