

def F(s):
    while "666" in s or "9909" in s or "66" in s:
        s = s.replace("666", "999", 1)
        s = s.replace("9909", "6", 1)
        s = s.replace("66", "0")
        
    return s

for n in range(4, 10_000):
    s = "9"+("6"*n)
    s2 = F(s)
    
    if len(s2) == 10:
        print(n)