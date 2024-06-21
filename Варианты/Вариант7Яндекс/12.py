
def F(s):
    while "8858" in s or "555" in s:
        if "8858" in s:
            s = s.replace("8858", "4", 1)
        else:
            s = s.replace("555", "58", 1)
        if "5858" in s:
            s = s.replace("5858", "85", 1)

    return s

maxn = 0

for n in range(3, 10_000+1):
    stri = "8"+"5"*n
    
    rs = sum(list(map(int, F(stri))))
    
    if n % 100 == 0:
        print(n)
    
    if rs == 66:
        maxn = max(maxn, n)
        print(n)
        
print("end")