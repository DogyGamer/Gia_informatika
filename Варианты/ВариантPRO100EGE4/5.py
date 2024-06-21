def perevod(n, base):
    res = []
    while n>0:
        res.append(n%base)
        n //= base
    return list(reversed(res))
def r(n):
    n4 = perevod(n, 4)
    if len(n4) % 2 == 0:
        n4.insert(len(n4) // 2, 0)
    
    return int("".join(list(map(str, n4))))


for i in range(2000):
    R = r(i)
    if R <= 180:
        print(i)

    
