lines = open("./9/4.csv", "r").readlines()

cntr = 0

for line in lines:
    line = list(map(int, line.replace("\n", "").split(";")))
    unique_angle = set(line)
    # print(unique_angle)
    if len(unique_angle) == 2 and sum(unique_angle) == 180:
        cntr +=1
        
print(cntr)