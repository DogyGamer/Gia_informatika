lines = open("9/3.csv", "r").readlines()
counter = 0
for line in lines:
    
    arr = list(map(int, line.split(";")))
    dic = {}
    for n in arr:
        if n in dic:
            dic[n] += 1
        else:
            dic[n] = 0
    
    povtoryauschiesya = [k for k,v in dic.items() if v == 1 ]
    nepovtor = [k for k,v in dic.items() if v == 0]
    if len(povtoryauschiesya) == 2:
        if(sum(nepovtor) / len(nepovtor)) < (sum(povtoryauschiesya) / len(povtoryauschiesya)):
            counter += 1     
        
    
print(counter)