lines = list(map(lambda x: list(map(int, x.replace("\n", "").split())), open("./26(4).txt", "r").readlines()))
n,m = lines[0]
lines = lines[1:]

arr = []

for s,d,t,l in lines:
    arr.append([s, d, t, True])
    if t+l > 24:
        arr.append([s, d, 24, False])
        arr.append([s, d+1, 0, True])
        arr.append([s, d+1, (t+l)-24, False])
    else:
        arr.append([s,d,t+l, False])
        
arr_by_day = {k:sorted([x for x in arr if x[1] == k], key=lambda x: x[2]) for k in range(1,32)}


counter = 0
maxcntr = 0
for k,v in arr_by_day.items():
    counter = 0
    maxcntr = 0
    for s,d,t,is_start in v:
        if is_start:
            counter += 1
            maxcntr = max(maxcntr, counter)
        else:
            counter -= 1 
    print(k, maxcntr)
    