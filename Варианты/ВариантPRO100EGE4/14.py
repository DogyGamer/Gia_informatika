def perevod(arr, base):
    res = 0
    arr = list(reversed(arr))
    for i in range(len(arr)):
        res += arr[i]*(base**i)
    return res        

for x in range(0, 19):
    a = perevod([7,8,x,7,9,6,4,3], 19)
    b = perevod([2,5,x,4,3], 19)
    c = perevod([6,3,x,5], 19)
    
    zna = a+b+c
    if zna % 18 == 0:
        print(x, zna// 18)