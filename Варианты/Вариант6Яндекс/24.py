text = open("./24(5).txt", "r").readlines()[0].replace("\n", "")

# text = "OOALALALOOKKALAL"

#  A, E, K, L, M, N, O, U. 

glasn = "AEOU"
sogls = "KLMN"

for gl in glasn:
    text = text.replace(gl, "!")

for sgl in sogls:
    text = text.replace(sgl, "?")

text = text.replace("!!", " ")
text = text.replace("??", " ")

text = text.split()

lens = []

maxln = 0
ptr = 0

for i in range(len(text)):
    ln = len(text[i])
    if i == 0 or i == len(text)-1:
        lens.append(ln+1)
        if ln+1 > maxln:
            maxln = ln+1
            ptr = i
    else:
        lens.append(ln+2)
        if ln+2 > maxln:
            maxln = ln+2
            ptr = i
            
print(maxln, ptr)