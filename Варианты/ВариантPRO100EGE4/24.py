line = open("./24_12476.txt", "r").readlines()[0].replace("\n", "")
line = line.replace("RO", "@").replace("O@", "O @").replace("@R", "@ R").split()

print([x for x in line if not("@@" in x) and x.count("@") == 21])
print(max([len(x)+21 for x in line if not("@@" in x) and x.count("@") == 21]))