def perevod(n, base):
    res = []
    if n == 0:
        return "0"
    while n > 0:
        res.append(n% base)
        n //= base
    return "".join(list(map(str, reversed(res))))

cntr = 0

for i in range(int("100000", 7), int("666666", 7)+1):
    n = perevod(i, 7)
    
    if n.count("0") == 1:
        if (n.count("2") + n.count("4") + n.count("6")) % 2 == 0:
            cntr += 1
        
print(cntr)
    
    