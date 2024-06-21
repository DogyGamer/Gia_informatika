from math import ceil

lines = list(map(int, open("./26(5).txt", "r").readlines()[1:]))

lines = sorted(lines)

print(lines)

res = [0]


for a in lines:
    if a >= ceil(res[-1] * 1.1):
        res.append(a)
        
        
print(res)

print([x for x in lines if x >= ceil(res[-1] * 1.1)])

print(len(res)-1)