def F(s):
    while not "00" in s:
        s = s.replace("01", "103", 1)
        s = s.replace("02", "2011", 1)
        s = s.replace("03", "130", 1)
        
    return s

for a1 in range(50):
    for a2 in range(50):
        for a3 in range(50):
            st = "0"+a1*"1"+a2*"2"+a3*"3"+"0"
            st2 = F(st)
            n1 = st2.count("1")
            n2 = st2.count("2")
            n3 = st2.count("3")
            if n1 == 92 and n2 == 16 and n3 == 52:
                print(a3)