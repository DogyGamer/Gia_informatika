from math import floor
ans = []
ans2 = []

n = 800_001


while len(ans) < 5:
    
    dels = []
    for i in range(2, floor(n**0.5)):
        if n % i == 0:
            del1 = i
            del2 = n // i
            if del1 != 14 and del2 != 14:
                if str(del1)[-1:-3:-1][-1:-3:-1] == "14":
                     dels.append(del1)
                if str(del2)[-1:-3:-1][-1:-3:-1] == "14":
                    dels.append(del2)
    
    if len(dels) > 0:
        print(n, min(dels))
        ans.append(n)
        ans2.append(min(dels))
    
    n += 1