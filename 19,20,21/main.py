from functools import lru_cache
import sys
sys.setrecursionlimit(5000)
def moves(h):
    if(h == 1):
        return [h+1]
    else:
        return h+1, h**2


@lru_cache(None)
def f(h):
    if(h >= 100):
        return 'END'
    elif(any(f(x) == 'END' for x in moves(h))):
        return 'P1'
    elif(all(f(x) == 'P1' for x in moves(h))):
        return 'V1'
    elif(any(f(x) == 'V1' for x in moves(h))):
        return 'P2'
    elif(all(f(x) == 'P2' or f(x) == 'P1' for x in moves(h))):
        return 'V2'

for i in range(1,99):
    print(i, f(i))