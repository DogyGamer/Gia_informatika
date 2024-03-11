lines = open("C:\\Users\\Admin\\Documents\\Школа\\ЕГЭ\\Информатика\\22\\1.txt", "r").readlines()[1:]

def prep(stri: str):
    stri_r = stri
    stri_r = stri_r.replace("\t\n", "")
    stri_r = stri_r.split("\t")

    
         
    return [int(stri_r[0]), int(stri_r[1]), list(map(int, stri_r[2].replace("\"", "").split(";"))) ]

data = {
    
}


lines = list(map(prep, lines))

with_zeros = [line for line in lines if line[2][0] == 0]
others = [line for line in lines if not line[2][0] == 0]

for line in with_zeros:
    data[line[0]] = line[1]

i = 0
length = len(others)
while length > 0:
    if i+1 >= length:
        i = 0
    else:
        i += 1
        
    print(len(others), length, i)
    line = others[i]
    
    
    if all([dep in data.keys() for dep in line[2]]):
        data[line[0]] = line[1] + sum([data[dep] for dep in line[2]])
        del others[i]
        length -= 1
        continue
    else:
        continue

print(data)
print(len([v for k,v in data.items() if v <= 170]))


# ANS
# 63 WRONG

# CORRECT
# 72