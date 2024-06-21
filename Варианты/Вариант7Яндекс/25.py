from math import floor


for i in range(397438, 443520+1):
    cntr = 0
    maxdel = 0
    for deli in range(2, floor(i**0.5)):
        if i % deli == 0:
            if deli % 2 == 0:
                cntr += 1
            if i // deli % 2 == 0:
                cntr += 1
                
            maxdel = max(maxdel, deli, i // deli)
            
    if cntr >= 142:
        print(cntr, maxdel)
        
        
# 143 201600
# 143 205920
# 143 207900
# 143 211680
# 143 214200
# 143 218400
# 167 221760