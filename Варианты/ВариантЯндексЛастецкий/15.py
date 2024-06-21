
def f(a,x,y):
    return (2*y > 5*x) or (x*y < a) or (x >= 22)


# for a in range(1000, 2000):
#     ress = []
#     for x in range(24):
#         for y in range(1000):
#             ress.append(f(a,x,y))
            
#     if all(ress):
#         print(a)
        
a = 1093
ress = []
for x in range(2000):
    for y in range(2000):
        ress.append(f(a,x,y))
        
if all(ress):
    print(a)