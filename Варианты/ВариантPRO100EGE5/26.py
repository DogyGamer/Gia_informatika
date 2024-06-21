lines = list(map(lambda x: list(map(int,  x.replace("\n", "").split())), open("./26_12933.txt", "r").readlines()))
N, K = lines[0]
lines = lines[1:]

arr = []
already_gathered = []
l = 0
r = N-1
conv = [-1]*N

for i in range(len(lines)):
    shlif, paint = lines[i]
    arr.append([i+1, shlif, True])
    arr.append([i+1, paint, False])
    
arr.sort(key=lambda x: x[1])
# print(arr)

while len(arr) > 0:
    id, time, is_shlif = arr.pop(0)
    if id in already_gathered:
        continue
    
    already_gathered.append(id)
    
    if is_shlif:
        conv[l] = id
        l += 1
    else:
        conv[r] = id
        r -= 1
    
# print(conv)
print(l, conv[K-1])