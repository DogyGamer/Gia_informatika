from itertools import product, permutations

sled = lambda a,b: 0 if a and not b else 1

def F(d):
    w = d["w"]
    x = d["x"]
    y = d["y"]
    
    return sled(x,y) and (w or (not w))


for perm in permutations("wxy"):
    for a1,a2,a3 in product([0,1], repeat=3):
        tb = [
            [1,1,0],
            [a1,1,a2],
            [1,0,1],
            [1,a3,1],
        ]
        ress = [0,0,1,1]
        
        anss = [F(dict(zip(perm, tb[i]))) == ress[i] for i in range(len(ress))]
        if(all(anss)):
            print("".join(perm))