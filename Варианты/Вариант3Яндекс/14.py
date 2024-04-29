
def perevod(i, base):
    res = []
    while i > 0:
        res.append(i % base)
        i //= base
    return list(reversed(res))

for i in range(201):
    in4 = perevod(i, 4)
    if len(in4) < 3:
        continue
    
    if "".join(list(map(str, reversed(in4[-1:-4:-1])))) == "123":
        print(i)
        
# 27
# 91
# 155