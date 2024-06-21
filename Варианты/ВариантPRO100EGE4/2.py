from itertools import permutations, product

sled = lambda a,b: 0 if a and not b else 1

def f(d):
    x = d["x"]
    y = d["y"]
    z = d["z"]
    w = d["w"]
    
    return (not sled(y, x==w)) and sled(z,x)

for perm in permutations("xyzw"):
    for a1,a2,a3,a4,a5 in product([1,0], repeat=5):
        tb = [
            [a1, 1, 1, a2],
            [0,a3,a4,0],
            [a5, 0,1,0]
        ]
        if all([f(dict(zip(perm, x)))==1 for x in tb]):
            print("".join(perm))