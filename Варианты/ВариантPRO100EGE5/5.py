def R(n):
    n2 = "".join(bin(n)[2:])
    if n % 3 == 0:
        r = n2.replace("0", "11")
    else:
        r = n2.replace("1", "10")
    return int(r, 2)


res = []
for i in range(1,5000):
    res.append(R(i))
    
print(max([x for x in res if x <= 161]))
