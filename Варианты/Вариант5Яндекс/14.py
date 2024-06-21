def perevod(base, arr):
    res = 0
    arr = list(reversed(arr))
    for i in range(len(arr)):
        res += arr[i] * (base**i)
    return res

maxsum = 0
ans = 0

for x in range(22):
    for y in range(22):
        a = perevod(22, [3,4,2,5,6,x,4])
        b = perevod(22,[7,2,8,4,7,y,3])
        
        if (a+b) % 125 == 0:
            if (x+y) > maxsum:
                maxsum = x+y
                ans = (a+b) / 125         
print(maxsum)
print(ans)