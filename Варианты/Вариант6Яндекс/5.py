
def r(n):
    binn = "".join(bin(n)[2:])
    res = ""
    if n % 2 == 0:
        res = "1"+binn+"1"
    else:
        res = binn+"10"
        
    return int(res, 2)


for n in range(1, 1000):
    rr = r(n)
    
    if rr > 179:
        print(n, rr)
        break