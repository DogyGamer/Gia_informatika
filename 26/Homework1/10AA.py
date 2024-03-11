    lines = list(map(lambda x: list(map(int, x.split())), open("./26/Homework1/26_10.txt", "r").readlines()[1:]))
lines.sort(key=lambda x: x[1])
dicti = {k:[] for k in set([x[0] for x in lines])}
for row, col in lines:
    dicti[row].append(col)
    

ans = {}
for row, cols in dicti.items():
    last_val = 0
    minind = 0 
    if(len(cols) >= 2):
        for col in cols:
            if col-last_val-1 == 13:
                minind = last_val+1
                break
            last_val = col
    if minind != 0:
        ans[row] = minind

print(dicti[max(ans.keys())])
print(max(ans.keys()), ans[max(ans.keys())])