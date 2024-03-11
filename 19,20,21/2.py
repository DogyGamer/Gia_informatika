from functools import lru_cache
from sys import setrecursionlimit

setrecursionlimit(100000000)
def moves(n):
    return n+1, n+3, n*2

@lru_cache(None)
def F(n):
    if n>= 42:
        return 'END'
    elif any([F(x) == 'END' for x in moves(n)]):
        return 'P1'
    elif all([F(x) == 'P1' for x in moves(n)]):
        return 'V1'
    elif any([F(x) == 'V1' for x in moves(n)]):
        return 'P2'
    elif all([F(x) == 'P1' or F(x) == 'P2' for x in moves(n)]):
        return 'V2'

for i in range(1, 42):
    print(i, F(i))