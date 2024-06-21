a = (3*3125**9) + (2*625**8) - (4*625**7) + (3*125**6) - (2*25**5) - 2024

def perevod(n, base):
    res = []
    while n > 0:
        res.append(n%base)
        n //= base
    return res

print(perevod(a,25).count(0))