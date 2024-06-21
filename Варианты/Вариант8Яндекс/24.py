s = open("./24(8).txt", "r").readlines()[0].replace("\n", "")
einds = []
minlen = float("inf")
for i in range(len(s)):
    if s[i] == "E":
        einds.append(i)
    

minlen = float("inf")

for i in range(len(einds)-239):
    start = i
    end = i+239
    leng = (einds[end] - einds[start]) + 1 
    minlen = min(minlen, leng)
    
print(minlen)

# 1156 - 1151 