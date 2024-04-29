from itertools import product, permutations

sled = lambda a,b: False if a and not b else True

def F(d):
    w = d["w"]
    x = d["x"]
    y = d["y"]
    z = d["z"]
    
    return sled(((w==1) == (not ((w and x) or y))), z)
r = []
for p in permutations("xyzw"):
    for a1,a2,a3,a4,a5,a6,a7,a8,a9,a10 in product([True, False], repeat=10):
        tb = [
            [a1,a2, 1, a3],
            [1, a4, 1, a5],
            [0, 1, 0, 0],
            [1, a6, 1, a7],
            [a8,a9, 1, a10],
        ]
        anss = [0,0,1,1,1]
        
        res = [F(dict(zip(p, tb[i]))) == anss[i] for i in range(len(anss))]
        if all(res):
            r.append(p)
        
        
print(set(p))