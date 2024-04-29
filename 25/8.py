# [101 000 000; 102 000 000]
import time
from math import floor

res = []
start = time.time()
for i in range(101_000_000, 102_000_000+1):
    if i % 100 == 0:
        precent = (i - 101_000_000) / 1_000_000
        if precent >= 1:
            end = time.time()
            print(end-start)
            print((end-start)*100)
            break
    
    if i % 2 != 0:
        continue
    
    if i % 4 == 0:
        continue
    
    i_2 = i // 2
    if floor(i_2 ** 0.5) ** 2 == i_2:
        a = floor(i_2 ** 0.5)
        flag = True
        for j in range(3, floor(a**0.5)):
            if a % j == 0:
                flag = False
                break
        if flag:
            res.append(i)
print(res)
print(len(res))