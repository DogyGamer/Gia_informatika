from itertools import permutations, product

def f(d):
    x = d["x"]
    y = d["y"]
    z = d["z"]
    w = d["w"]
    
    return (x and y) or ((z==y) and w)

res = []

for perm in permutations("xyzw"):
    for arrr in product([True, False], repeat=7):
        a1,a2,a3,a4,a5,a6,a7 = arrr
        tb = [
            [a1,a2,True,True],
            [a3,False,False,a4], 
            [a5,False,a6,False],
            [a7,False,False,False]
        ]
        anses = [False,False,True,True]
        
        ans = [f(dict(zip(perm, tb[i]))) == anses[i] for i in range(len(tb))]
        if all(ans):
            res.append("".join(perm))
            
cnts = {x:0 for x in set(res)}

for a in res:
    cnts[a] += 1
    
print(cnts)