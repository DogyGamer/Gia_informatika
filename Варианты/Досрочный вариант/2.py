from itertools import permutations, product

def F(d):
    x = d["x"]
    y = d["y"]
    z = d["z"]
    w = d["w"]
    
    return (x and (not y)) or (y == z) or w    


for perm in permutations("xyzw"):
    for a1,a2,a3,a4,a5 in product([0,1], repeat=5):
        tb = [
            [a1, 0,a2,0],
            [a3,0,a4,1],
            [1,0,a5,1]
        ]
        
        if all([F(dict(zip(perm, t))) == 0 for t in tb]):
            print("".join(perm))