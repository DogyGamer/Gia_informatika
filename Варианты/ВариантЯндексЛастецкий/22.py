lines = open("./22.txt", "r").readlines()

arr = []

for line in lines:
    line = line.replace("\n", "")
    line = [x for x in line.split("\t") if len(x) > 0]
    id = int(line[0])
    t = int(line[1])
    deps = list(map(int, line[2].replace("\"", "").split(";")))
    # print(deps)
    arr.append([id, t, deps])
    
d = {0:0}

while len(arr) > 0:
    c = arr.pop(0)
    id,t,deps = c
    # print(id)
    if all([x in d.keys() for x in deps]):
        maxt = max([d[x] for x in deps])
        d[id] = maxt + t
    else:
        arr.append(c)
        
print(max([x for x in d.values()]))
    