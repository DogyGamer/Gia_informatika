from itertools import product, permutations

def F(d):
    x = d["x"]
    y = d["y"]
    z = d["z"]
    
    return (not z) and x or x and y

for perm in permutations("xyz"):
    print("\n", "".join(perm))
    for a1,a2,a3 in product([0,1], repeat=3):
        print(a1,a2,a3,F(dict(zip(perm, [a1,a2,a3]))))