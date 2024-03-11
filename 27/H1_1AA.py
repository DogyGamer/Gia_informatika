lines = open("./27/H1_1_B.txt", "r").readlines()[1:]
lines = [list(map(int, x.split())) for x in lines]

S = 0
min_diff = 999_999_999

for line in lines:
    a, b = line
    S += max(a,b)
    if a % 3 != b % 3:
        min_diff = min(min_diff, max(a,b)-min(a,b))
        
if S % 3 == 0:
    S -= min_diff
    
print(S)