from itertools import product

res = []
for word in list(product([4,5], repeat=9)):
    if word[0] == 4 or word[-1]== 4:
        continue
    flag = True
    for i in range(1,8):
        if word[i] == 4:
            if not (word[i-1] == 4 or word[i+1] == 4):
               flag = False 
               break
        
    if flag:
        res.append(word)
        
print(len(res), len(set(res)))
print(res)
ans = 0
for word in res:
    ans2 = 1
    for x in word:
        ans2 *= x
    ans += ans2            
print(ans)