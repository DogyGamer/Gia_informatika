# 424 242

i = 424_242

cntr = 0

from math import floor

def findfdel(i):
    for j in range(2, int(i **0.5)):
        if i % j == 0:
            return j
            
    return -1

while cntr <= 8:
    
    dels = findfdel(i)
    # print(i, dels)
        
    if dels == -1:
        i += 1
        continue
    
    M = dels + (i//dels)
    if M % 2024 == 42:
        print(i, M)
        cntr += 1
    
    
    i+= 1
    
    
# 425120 212562
# 425157 141722
# 425225 85050
# 429053 6114
# 429168 214586
# 431229 143746
# 433216 216610
# 437264 218634