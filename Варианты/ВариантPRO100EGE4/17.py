lines = list(map(lambda x: int(x.replace("\n", "")), open("./17_12471.txt", "r").readlines()))

mhuy = max([x for x in lines if str(x)[-1:-3:-1][::-1] == "13"])

print(mhuy)

cntr = 0
summ = 0

for i in range(0, len(lines)-2):
    tr = lines[i:i+3]
    
    if not (all([x% 2 == 0 for x in tr]) or any([len(str(x)) == 2 for x in tr])):
        continue
    
    if sum(tr) <= mhuy:
        cntr += 1
        summ += sum(tr)
    
print(cntr, summ/cntr)