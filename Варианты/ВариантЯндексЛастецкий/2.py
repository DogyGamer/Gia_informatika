from itertools import permutations, product

sled = lambda a,b: 0 if a and not b else 1

def F(d):
    x = d["x"]
    y = d["y"]
    z = d["z"]
    w = d["w"]
    
    return sled((w==1), z) and ((not y) and x)
    

for perm in permutations("wxyz"):
    for a1, a2,a3,a4 in product([True, False], repeat=4):
        tb = [
            [0,0,1,a1],
            [0,1,1,0],
            [a2,a3,1,0],
            [0,a4,1,0]
        ]
        res = [0,0,0,1]
        if all([F(dict(zip(perm, tb[i]))) == res[i] for i in range(len(tb))]):
            print("".join(perm))