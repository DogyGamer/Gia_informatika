a = (15 * (2401**1500)) - (10*(343*1200)) + (40*(49**1000)) - (35*(7**850)) - 4805

def perevod(n, base):
    res = []
    while n > 0:
        res.append(n%base)
        n //= base
        
    return list(reversed(res))

print(len([x for x in perevod(a, 49) if x > 9]))

print([x for x in perevod(a, 49) if x > 9])

# print(perevod(a, 49))

