def perevod(n, base):
    res = []
    if n == 0:
        return "0"
    while n > 0:
        res.append(n% base)
        n //= base
    # return "".join(list(map(str, reversed(res))))
    return list(reversed(res))

a = (625**90) + (125**120) - (5 * 25)

arr = perevod(a, 25)

print(sum([b for b in arr if b % 2 == 0]))
