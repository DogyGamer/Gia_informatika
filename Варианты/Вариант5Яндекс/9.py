lines = open("./9(3).csv", "r").readlines()

cntr = 0

for line in lines:
    line = sorted(list(map(int, line.replace("\n","").split(";"))), reverse=True)
    if line[1] - line[-2] == 20:
        cntr += 1
    
print(cntr)