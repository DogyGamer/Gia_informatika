a = (18*(7**108))-(5*(49**76))+(343**35)-50

def perevod(n, base):
    res =[]
    while n > 0:
        res.append(n % base)
        n //= base
    return list(reversed(res))

print(a)
print([x for x in perevod(-a, 49) if x > 0])
print(sum(perevod(-a, 49)))

# 1134