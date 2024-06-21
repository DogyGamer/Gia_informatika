def perevod(n,base):
    res = []
    while n > 0:
        res.append(n% base)
        n //= base
    
    return list(reversed(res))

def R(n):
    n3 = perevod(n, 3)
    
    if sum(n3) % 2 == 0:
        n3.append(0)
        n3.pop(0)
        n3.pop(0)
        n3.insert(0,2)
        # n3[-2] = 2
    else:
        n3.append(1)
        n3[0] = 2
        n3[1] = 0
        
    return int("".join(list(map(str, n3))), 3)



for i in range(8,100):
    r = R(i)
    if r > 75:
        print(i, r)