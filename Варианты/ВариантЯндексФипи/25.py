import fnmatch

res = []

for i in range(10):
    for j in range(10):
        n = int(f"12345{i}7{j}8")
        if n % 31 == 0:
            res.append(n)
            
for x in sorted(res):
    print(x, x//31)
    
# 123452788 3982348
# 123453718 3982378
# 123457748 3982508