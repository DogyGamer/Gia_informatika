from itertools import permutations, product

def f(d):
    k = d["k"]
    l = d["l"]
    m = d["m"]
    n = d["n"]
    
    return (not n) or k and (not m) or (l==m)

for perm in permutations("klmn"):
    for a1,a2,a3,a4 in product([1,0], repeat=4):
        tb = [
            [0,1,0,a1],
            [a2,0,0,a3],
            [1,0,a4,1]
        ]
        
        res = [f(dict(zip(perm, x))) == 0 for x in tb]
        if all(res):
            print(perm)        