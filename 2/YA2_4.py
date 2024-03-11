from itertools import permutations, product, combinations_with_replacement

sled = lambda a,b: False if a and not b else True
def F(dicti):
    a = dicti["a"]
    b = dicti["b"]
    c = dicti["c"]
    d = dicti["d"]
    
    return sled((a and b), c) and sled((b and c), d)

res = []

for perm in list(permutations(["a","b","c","d"])):
    for a1,a2,a3,a4,a5,a6 in product([True, False], repeat=6):
        arr = [
            [a1, True, True, True],
            [a2, True, a3, True],
            [True, True, True, a4],
            [a5, True, True, a6]
        ]
        list_dicts = [F(dict(zip(perm, x))) == False for x in arr]
        if all(list_dicts):
            print(perm)
            res.append(perm)
            
print(set(res))
        
    
        