lines = open("./26/26_3.txt", "r").readlines()[1:]
# lines = [list(map(int, x.split())) for x in lines]

data = []

for line in lines:
    start, end = list(map(int, line.split()))
    data.append([start, True])
    data.append([end, False])
    
data.sort(key=lambda x: x[0])


curr_cntr = 0
time_cntr = 0
empty_cntr = 0
for i in range(len(data)):
    time, is_start = data[i]
    if is_start:
        curr_cntr += 1
    else:
        curr_cntr -= 1
        
    if curr_cntr == 0:
        empty_cntr += 1
        if i+1 > len(data)-1:
            time_cntr += 1439-time
        else:
            time_cntr += data[i+1][0]-1-time
        
print(empty_cntr, time_cntr+25)