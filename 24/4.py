glasns = "AEIOUY"

line = open("./24/24_4.txt", "r").readlines()[0]

# line = "AEKZIOPSW"
print(line)

max_len = 0
currlen = 1
was_glasn = False
for i in range(1,len(line)):
    symb = line[i]
    prev_symb = line[i-1]
    
    if (symb > prev_symb):
        if symb in glasns:
            if not was_glasn:
                currlen += 1
                max_len = max(max_len, currlen)
                was_glasn = True
            else:
                currlen = 1
                was_glasn = True
        else:
            currlen += 1
            max_len = max(max_len, currlen)
    else:
        if symb in glasns:
            was_glasn = True
        else:
            was_glasn = False
        currlen = 1

print(max_len)