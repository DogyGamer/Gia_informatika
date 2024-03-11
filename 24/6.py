line = open("./24/24_6.txt", "r").readlines()[0].replace("\n", "")

start_slice = 0

len_max = 0

for i in range(1,len(line)):
    slice = line[start_slice:i]
    len_max = max(len_max, i-start_slice)
    symb = line[i]
    if line[i] in slice:
        start_slice = start_slice+slice.index(symb) + 1
        

print(len_max)
    