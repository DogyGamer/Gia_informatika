
def R(n):
    arr = list(map(int, str(n)))
    
    t = sum(arr)
    
    res = []
    for a in arr:
        res.append(t%a)
    
    return int("".join(list(map(str, sorted(res, reverse=True)))))

for n in range(1000, 9999):
    if "0" in str(n):
        continue
    r = R(n)
    if r > 2000:
        print(n, "\t", r)