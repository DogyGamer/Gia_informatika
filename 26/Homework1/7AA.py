lines = list(map(int, open("./26/Homework1/26_7.txt", "r").readlines()[1:]))

lmax = 0
cntr = 0

set_lines = set(lines)

for i in range(len(lines)-1):
    for j in range(i+1, len(lines)):
        summa = lines[i]+lines[j] 
        if summa%2 != 1:
            if(summa in set_lines):
                cntr += 1
                lmax = max(lmax, summa)    
            


print(cntr, lmax)