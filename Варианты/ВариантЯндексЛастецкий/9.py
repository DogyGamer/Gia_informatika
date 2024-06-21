lines = open("./9.csv", "r").readlines()

lines = list(map(lambda x: list(map(int, x.replace("\n", "").replace("\ufeff", "").split(";"))), lines))
cntr = 0
for line in lines:
    a,b,c = line

    if len(line) == len(set(line)):
        if a<b and b<c:
            cntr += 1
            
print(cntr)