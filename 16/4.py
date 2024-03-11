from sys import setrecursionlimit
from functools import lru_cache

@lru_cache()
def F(n):
    if n>10_000:
        return 42
    elif n <= 10_000 and n %2 != 0:
        return -( n + F(n+1) + F(n+3) )
    elif n <= 10_000 and n % 2 == 0:
        return 2*n + F(n+3) + F(n+4) + F(n+6)
    
a = F(9994)
print(a)
b = F(9996)
print(b)
print(b-a)
print(F(9996) - F(9994))