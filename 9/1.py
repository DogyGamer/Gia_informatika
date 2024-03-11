strings = open("9\\1.csv", "r").readlines()


coutner = 0

for line in strings:
    arr = list(map(int, line.split(";")))
    print(arr)
    vals = {}
    povtors = []
    for val in arr:
        if val in vals.keys():
            vals[val] += 1
            povtors.append(val)
        else:
            vals[val] = 1
    if(len(arr) != len(set(arr))):
        
        if ((sum(set(arr)) - sum(povtors)) % 2 != 0):
            coutner += 1 

print(coutner)