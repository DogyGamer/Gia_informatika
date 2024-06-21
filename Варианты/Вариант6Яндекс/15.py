
prin = lambda x, start,end: x >= start and x <= end

sled = lambda a,b: 0 if a and not b else 1

b = [74, 194]
c = [152, 223]

def f(x,a):
    op1 = (not prin(x, *a)) and (prin(x, *b))
    op2 = prin(x, *b)
    op3 = (not prin(x, *c))
    
    return sled(op1, sled(op2, op3))

lenmn = lambda st,en: (en+1)-st

res = []

for start in range(300):
    for end in range(start+1, 302):
        if not (start < end):
            continue
        
        a = [start, end]
        if all([f(x,a) == 1 for x in range(500)]):
            res.append([lenmn(*a), a])
            
print(min(res, key=lambda x: x[0]))

# 43