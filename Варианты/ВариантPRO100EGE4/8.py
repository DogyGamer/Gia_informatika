from itertools import product


res = []
for a1,a2,a3 in product([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15], repeat=3):
    if a1 > a2 and a2 > a3:
        res.append("/".join(list(map(str, [a1,a2,a3]))))
        
for a1,a2,a3,a4,a5 in product([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15], repeat=5):
    if a1 > a2 and a2 > a3 and a3 > a4 and a4 > a5:
        res.append("/".join(list(map(str, [a1,a2,a3, a4,a5]))))
        
print(res)
print(len(res), len(set(res)))