lines = list(map(lambda x: list(map(int, x.replace("\n", "").split())), open("./26_12478.txt", "r").readlines()))

n,start_ege, end_ege = lines[0]
lines = [ [start, end] for start,end in sorted(lines[1:], key=lambda x: x[1], reverse=True) if start < end_ege and end > start_ege]

cntr = 1
gathered = [lines[0]]
# for i in range(2, len(lines)):
#     start, end = lines[i]

lines = lines[1:]
print(gathered[-1][0], start_ege)
while gathered[-1][0] > start_ege:
    udovl_line = [[start, end] for start, end in lines if start < gathered[-1][1] and end >= gathered[-1][0]]
    new_nabl = sorted(udovl_line, key=lambda x: x[0])[0]
    gathered.append(new_nabl)



print(len(gathered), gathered[-1][1]-start_ege)


print(max([end-start_ege for st, end in lines if st < start_ege and end >= gathered[-2][0]]))