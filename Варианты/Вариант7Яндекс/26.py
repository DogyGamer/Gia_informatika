lines = list(map(lambda x: list(map(int, x.split())), open("./26(6).txt", "r").readlines()[1:]))

arr = []

for i in range(len(lines)):
    shlif, paint = lines[i]
    arr.append([i+1, shlif, True])
    arr.append([i+1, paint, False])

arr = sorted(arr, key=lambda x: x[1], reverse=True)
    
# print(arr)

already_gathered = []
last_raspred = [-1, -1]

res = [-1]*len(lines)

l = 0
r = -1

while len(arr) > 0:
    ind, time, is_shlif = arr.pop()
    if ind in already_gathered:
        continue
    
    already_gathered.append(ind)
    if is_shlif:
        res[l] = ind
        last_raspred = [ind, l]
        l += 1
    else:
        res[r] = ind
        last_raspred = [ind, r]
        r -= 1

print(res, last_raspred)



# >>> a = [1,1,1] 
# >>> a.insert(0,2) 
# >>> a.append(3) 
# [2, 1, 1, 1, 3]