line = open("./24.txt", "r").readlines()[0]

arr = []
cntr = 0

start = 0

maxlen = 0

# for i in range(len(line)):
for i in range(len(line)):
    if line[i] == "A":
        arr.append(i)
        if len(arr) > 240:
            start = arr.pop(0)
            # print(f"{i} more than 240 a in array new start {start} ")
        # else:
            # print(f"new a cuurent length {len(arr)}")
    # else:
        # print(f"{i} letter not a curr length {(i-start)+1}")
    maxlen = max(maxlen, (i-start)+1)
    
print(maxlen)