def perevod(base, n):
    N = n
    res = []
    while N > 0:
        res.append(N % base)
        N //= base
    return list(reversed(res))


for i in range(10,1000):
    n_5 = perevod(5, i)
    ost = i % 25
    if ost == 0:
        n_5.extend(list(reversed(n_5[-1:-4:-1])))
    else:
        n_5.extend(perevod(5, ost))
    
    str_n = "".join(map(str, n_5))
    R = int(str_n, 5)
    if (R > 10000):
        print(i, str_n, R)
    
print(perevod(5,25))
        