lines = list(map(lambda x: int(x.replace("\n", "")), open("./27-B_12934.txt", 'r').readlines()))
K = lines[0]
lines = lines[2:]


l = 0
r = 1

curr_s = lines[l]+lines[r]

max_s = 0

while l < len(lines)-1:
    start_val = lines[l]
    if r+1 > len(lines)-1:
        break
    next_val = lines[r+1]
    if curr_s+next_val <= K:
        curr_s += next_val
        r+=1
    else:
        curr_s -= start_val
        l += 1
    
    max_s = max(max_s, (r-l)+1)
    


# print(lines)
print(max_s)
# Это можно сделать за линию с одним указателем