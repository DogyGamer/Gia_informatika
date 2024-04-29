# line = open("./27_A.txt", "r").readlines()[0]
# 1 - 34
line = "5653410342121"

res = 1
prev = 0
for i in range(len(line)-1):
    lcntr = 0
    if int(line[i]) != 0:
        lcntr += 1
        if int(line[i:i+2]) <= 34:
            lcntr += 1
    if prev == 2 and lcntr == 2:
        lcntr -= 1
    prev = lcntr
    if lcntr != 0:
        res *= lcntr
    
print(res)