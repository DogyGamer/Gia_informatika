from functools import lru_cache
from sys import setrecursionlimit
setrecursionlimit(5000)

@lru_cache()
def moves(h):
    return h+1, h+2, h*3


@lru_cache()
def f(S):
    if S >= 74:
        return "END"
    elif any([f(x) == "END" for x in moves(S)]):
        return "P1"
    elif all([f(x) == "P1" for x in moves(S)]):
        return "V1"
    elif any([f(x) == "V1" for x in moves(S)]):
        return "P2"
    elif all([f(x) == "P1" or f(x) == "P2" for x in moves(S)]):
        return "V2"
    else: return "0"
    
    
for S in range(1, 74):
    print(S, f(S))