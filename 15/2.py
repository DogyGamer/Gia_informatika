def F(a, x,y):
    return((x + 2*y)  < a) or (y>x) or (x> 20)

for A in range(0, 1000):
    if all([F(A,x,y) for x in range(1000) for y in range(1000)] ):
        print(A)
        
        