arr = list(map(int, open("./17.txt", "r")))


max42 = max([x for x in [y for y in arr if len(str(y)) > 2] if str(x)[-1] == "2" and str(x)[-2]=="4"]) ** 2

maxmult = 0
cntr =0

# aaa = [x for x in arr if len(str(x)) < 2]
# print(aaa)

for i in range(len(arr)-2):
    line = arr[i:i+3]
    
    if len([x for x in [y for y in line if len(str(y)) > 1] if str(x)[-1] == "2" and str(x)[-2] == "4" ]) >= 2:
        mult = line[0] * line[1] * line[2]
        if mult > max42:
            cntr += 1
            maxmult = max(maxmult, mult)
    
print(cntr, maxmult)
    