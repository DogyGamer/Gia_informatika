a = (7 * (49**120)) - (6 * (343**65)) - (5 * (7**40))

def perevod(n, base):
    res = []
    while n > 0:
        res.append(n % base)
        n //= base
    
    return list(reversed(res))

print(perevod(a, 7).count(6))