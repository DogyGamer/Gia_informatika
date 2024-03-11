lines = open("./17/17_3.txt", "r").readlines()
lines = list(map(int, lines))

cntr = 0
min_pr = 999_999_999

for i in range(2, len(lines)-3):
    curr_pair = lines[i]+lines[i+1]
    l_p = lines[i-1]+lines[i-2]
    r_p = lines[i+2]+lines[i+3]
    if l_p > 0 and r_p > 0 and curr_pair > 0:
        if curr_pair > l_p and curr_pair > r_p:
            cntr += 1
            min_pr = min(min_pr, lines[i]*lines[i+1])
            
print(cntr, min_pr)