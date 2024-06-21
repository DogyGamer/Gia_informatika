line = open("./24(9).txt", "r").readlines()[0].replace("\n", "")

line = line.replace("A", "@").replace("B", "@").replace("C", "@")


# line = "0@@000@0"

line = line + "@@"

start = 0
mxlen = 0
for i in range(len(line)-1):
    a = line[i]
    b = line[i+1]
    if a == "@" and b == "@":
        
        mxlen = max(mxlen, (i-start)+1)
        start = i+1
        
print(mxlen)