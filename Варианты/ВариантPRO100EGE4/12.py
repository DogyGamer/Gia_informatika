def f(s):
    while "01" in s or "02" in s or "03" in s:
        s = s.replace("01", "30", 1)
        s = s.replace("02", "3103", 1)
        s = s.replace("03", "1201", 1)
    return s

def pr(s):
    # print("1: ", s.count("1"))
    # print("2: ", s.count("2"))
    # print("3: ", s.count("3"))
    
    return s.count("1"),  s.count("2"), s.count("3")

pr(f("0"+"1"*10+"2"*13+"3"*2))

from itertools import permutations


b1 = "1"
b2 = "2"
b3 = "3"
for a1 in range(1,30):
    for a2 in range(1,30):
        for a3 in range(1,30):
            s = "0"+b1*a1+b2*a2+b3*a3
            res = pr(f(s))
            
            if res[0] == 31 and res[1] == 24 and res[2] == 46:
                print(a1,a2,a3)