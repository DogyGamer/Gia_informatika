def F(n):
    binn = bin(n)[2:]
    res = ""
    if n % 2 ==0:
        res = binn+"01"
    else:
        res = "1"+binn+"1"
    
    return int(res, 2)

for n in range(12, 50):
    r = F(n)
    if r > 156:
        print(n, r)