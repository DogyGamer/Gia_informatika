a = (2**2048) + (32**102) - (8*(4**128))

def perevod(n, base):
    res = []
    while n > 0:
        res.append(n % base)
        n //= base
    
    return list(reversed(res))

print(len([x for x in perevod(a, 32) if x > 9]))