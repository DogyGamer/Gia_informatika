def f(d):
    x = d["x"]
    y = d["y"]
    z = d["z"]
    w = d["w"]
    
    return (x or (not y)) and (not (y == z)) and (not w)


from itertools import permutations, product


for perm in permutations("xyzw"):
    for a1,a2,a3,a4 in product([0,1], repeat=4):
        tb = [
            [1,1,a1,a2],
            [a3,1,0,0],
            [1,a4,1,0]
        ]

        if all([f(dict(zip(perm, x))) == 1 for x in tb]):
            print("".join(perm))