
resa = []
for A in range(1000):
    anses = []
    for x in range(500):
        for y in range(500):
            res = ((3*x + y) > A) and (y < x) and (x < 30)
            anses.append(not res)
        
    if all(anses):
        print(A)    
        resa.append(A)
        
print(resa)