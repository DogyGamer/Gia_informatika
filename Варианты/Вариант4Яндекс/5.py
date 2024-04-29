def perevod(n, base):
    res = []
    if n == 0:
        return "0"
    while n > 0:
        res.append(n% base)
        n //= base
    return "".join(list(map(str, reversed(res))))

def R(N):
    n3 = perevod(N, 3)
    n3 += perevod(n3.count("2"), 3)
    n3 += perevod(n3.count("1"), 3)
    n3 += perevod(n3.count("0"), 3)
    # print(n3)
    return int("".join(n3), 3)


for n in range(2000):
    r = R(n)
    if r < 1000:
        print(n, r)
        