

# 1000,2000
for i in range(1000,2000):
    a = list(map(int, list(str(i))))
    if len(a) != len(set(a)):
        continue
    
    b = max(a) + min(a)
    c_1 = [x for x in a if x != max(a) and x != min(a)]
    c = c_1[0]*c_1[1]
    
    d = int(str(min(b,c))+str(max(b,c)))
    # print(d)
    if d > 85:
        print(i, d)
    
    