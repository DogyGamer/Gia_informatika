def perevod(a, base):
    s = 0
    a = list(reversed(a))
    for i in range(len(a)):
        s += a[i] * (base**i)

    return s

for x in range(29):
    a = perevod([4,2,x,1,5,8], 29)
    b = perevod([1,6,x,2,3,4], 29)
    
    r = a+b
    if r % 28 == 0:
        print(x, r, r/28)
    
    