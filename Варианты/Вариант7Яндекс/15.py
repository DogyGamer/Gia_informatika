
def F(a,x,y):
    return ((x>= a) or (121 >= x**2)) and ((y**2 < 49) or (a < y))


for a in range(1000):
    res = []
    for x in range(50):
        for y in range(50):
            res.append(F(a,x,y))
            
    if all(res):
        print(a)