def perevod(list, base):
    res = 0
    for i in range(len(list)):
        res += list[i]*(base**i)

    return res

lmax = 0

for y in range(0,14):
    for x in range(0,14):
        a = perevod([1,4,y,5,x,2], 14)
        b = perevod([3,1,x,2,y,3], 14)
        
        if (a+b) % 9 == 0:
            lmax = max(lmax, a+b)
            
print(lmax // 9)