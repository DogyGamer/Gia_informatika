from math import floor
import time

res = []
for i in range(1_000_000,2_000_000+1):
    cntr_lw_100 = 0
    
    
    for j in range(floor(i**0.5), 0, -1):
        if i % j != 0:
            continue
        
        first = j
        second = i // j
        diff = abs(second - first)
        if diff <= 100:
            cntr_lw_100 += 1
        else:
            break
        
    if cntr_lw_100 >= 3:
        res.append(i)
        
print(res)
print(len(res))
        
