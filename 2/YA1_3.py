from itertools import permutations

sled = lambda a,b: False if a and not b else True

def F(dict):
    a = dict["a"]
    b = dict["b"]
    c = dict["c"]
    d = dict["d"]
    return sled(a,b) and sled(b,c) and sled(c,d)

    

for a1 in [True, False]:
    for a2 in [True, False]:
        arr = [
            [False, a1, True, False],
            [False, a2, True, False],
            [False, True, True, True],
        ]
        for perm in set(permutations("abcd")):
            dicts = [F(dict(zip(perm, x))) for x in arr]
            if(all(dicts)):
                print(perm)