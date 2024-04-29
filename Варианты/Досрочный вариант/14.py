a = 3*(5103**2020) + 3*(729**2021) - 2*(343**2022) + 27**2023 - 4*(7**2024) - 2029

def perevod(n, base):
    res = []
    
    while n > 0:
        res.append(n % base)
        n //= base
        
    return list(reversed(res))

print(len([x for x in perevod(a, 27) if x > 9]))