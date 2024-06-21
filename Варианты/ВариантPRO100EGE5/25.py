import fnmatch
from math import floor

n = 1

while n * 2024 <= 10**10:
    n2 = n * 2024
    if fnmatch.fnmatch(str(n2), "1?2*4"):
        if floor(n2**0.5)**2 == n2:
            print(n2, n)
    
    n+= 1
    
# 1024144 506
# 1327290624 655776
# 1721586064 850586