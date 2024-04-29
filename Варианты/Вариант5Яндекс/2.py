from itertools import permutations, product

sled = lambda a,b: 0 if a and (not b) else 1

def F(d):
    x = d["x"]
    y = d["y"]
    w = d["w"]
    return (x and sled(w,y)) == 1

# def F(x,y,w):
#     return (x and (sled(w,y))) == 1

for perm in permutations("wxy"):
    print("\n")
    print(perm)
    print(*perm,"F", sep="\t")
    for aa in product([0,1], repeat=3):
        da = dict(zip(perm, aa))
        print(da[perm[0]],da[perm[1]],da[perm[2]], 1 if F(da) else 0, sep="\t")
        
# for a in product([0,1], repeat=3):
#     print(a[0],a[1],a[2], 1 if F(a[1], a[0], a[2]) else 0, sep="\t")