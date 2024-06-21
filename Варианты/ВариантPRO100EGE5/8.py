from itertools import permutations


cntr = 0
res = []
for word in permutations("ПРОСТО"):
    word = "".join(word)
    if "ОО" in word:
        # print(word)
        continue
    else:
        res.append(word)
        cntr+= 1
        
        
print(len(set(res)))
print(cntr)