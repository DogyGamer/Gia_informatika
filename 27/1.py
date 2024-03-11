lines = open("27\\1-A.txt", "r").readlines()

def prep(stri:str):
    return int(stri.replace("\n", ""))

lines = list(map(prep, lines))

cntr = 0

for i in range(len(lines)):
    for j in range(i+1, len(lines)):
        if (j-i) % 9 == (lines[i]+lines[j]) % 9:
            cntr +=1
            
print(cntr)


# Ускорить решение, вторую часть сделать таким путем не выйдет