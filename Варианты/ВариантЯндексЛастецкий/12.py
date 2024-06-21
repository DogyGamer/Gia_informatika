def F(s):
    while "9999" in s or "933" in s or "3339" in s:
        if "9999" in s:
            s = s.replace("9999", "3", 1)
        if "933" in s:
            s = s.replace("933", "55", 1)
        if "3339" in s:
            s = s.replace("3339", "93", 1)
            
    return s
for n in range(4, 10000):
    s = "3"+(n*"9")
    if n % 100 == 0:
        print(f"\t{n}/10000 = {(n/10000)*100}%")
    s2 = list(map(int, F(s)))
    if sum(s2) == 70:
        print(n)
    