from functools import lru_cache
from sys import setrecursionlimit
setrecursionlimit(10000000)


@lru_cache(None)
def F(n):
    if n <= 2:
        return 1
    else:
        return F(n-2) * (n-1)
    

print(F(8))