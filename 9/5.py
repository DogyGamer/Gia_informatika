lines = open("./9/5.csv", "r").readlines()[10:]
lines = [x.replace("\n", "").split(";") for x in lines]

cntr = 0

for line in lines:
    temp = float(line[1].replace(",", "."))
    feel_temp = float(line[2].replace(",", "."))
    degree = int(line[5])
    
    if not (temp-feel_temp >= 5):
        continue
    
    if (degree >= 0 and degree <= 45) or (degree >= 315 and degree <= 360):
        cntr += 1 
        
print(cntr)