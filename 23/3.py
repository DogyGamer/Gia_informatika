

def F(n, cmd, is_73gotten):
    
    if cmd == 1:
        n += int(str(n)[0])    
    elif cmd == 2:
        n += 3
    elif cmd == 3:
        n = (2*n)-1
        
    if n == 73:
        is_73gotten = True
    
    if n == 81:
        return 0
    
    if n == 89:
        if is_73gotten:
            return 1
        else:
            return 0
    elif n < 89:
        lcntr = 0
        lcntr += F(n, 1, is_73gotten)
        lcntr += F(n, 2, is_73gotten)
        lcntr += F(n, 3, is_73gotten)
        return lcntr
    else:
        return 0
    

print(F(42, 0, False))