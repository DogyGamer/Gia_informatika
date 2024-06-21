a = (3*(3125**8)) + (2 * (625**7)) - (4*(625**6)) + (3 * (125**5)) - (2*(25**4)) - 2024

def perevod(n, base):
    res = []
    while n > 0:
        res.append(n % base)
        n //= base
    return res[::-1]

print(perevod(a, 25).count(0))