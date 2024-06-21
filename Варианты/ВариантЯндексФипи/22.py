# lines = list(map(lambda x: list(map(int, x.replace("\n", "").split("\t"))), open("./22(9).csv").readlines()))
lines = open("./22(9).txt").readlines()
lines = list(map(lambda x: x.split("\t"), lines))

d = {0:0}

arr = []

for id, t, dep in lines:
    id = int(id)
    t = int(t)
    dep = list(map(int, dep.replace("\"", "").replace("\n", "").split(";")))
    
    arr.append([id,t,dep])


while len(arr) > 0:
    id,t,dep = arr.pop(0)
    if all([x in d.keys() for x in dep]):
        d[id] = max([d[x] for x in dep]) + t
    else:
        arr.append([id,t,dep])
        
print(max(d.values()))