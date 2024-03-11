from functools import lru_cache



@lru_cache()
def F(N):
    if N <= 2:
        return 2
    else:
        return 3 * F(N-1) - F(N-2)
    
    
print(F(6))