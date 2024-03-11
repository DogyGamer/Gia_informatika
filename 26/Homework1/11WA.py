
# a = [[0 for i in range(10_000)] for i in range(10_000)]
# print("Array_created")

a = list(map(lambda x: list(map(int, x.split())), open("./26/Homework1/26_11.txt", "r").readlines()[1:]))
a.sort(key=lambda x: x[1])
dicti = {x[0]:[] for x in a}
for item in a:
    # print(item[0])
    dicti[item[0]].append(item[1])
    
ans = {}

for row in dicti.keys():
    lmax_len = 0
    last_len = 0
    last_val = 0
    for value in dicti[row]:
        if value-last_val <= 1:
            if last_len == 0:
                last_len = 2
            else:
                last_len += 1
                
            lmax_len = max(lmax_len, last_len)
        else:
            last_len = 0
            
        last_val = value
    if lmax_len > 2:
        ans[row] = lmax_len
    
print(ans)
print(dicti[2786])
    