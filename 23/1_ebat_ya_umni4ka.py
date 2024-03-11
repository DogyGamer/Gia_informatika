counter = 0


def F(n, cmd, isnine_gotten):
    is_nine = isnine_gotten
    new_n = n
    if(cmd == 1):
        new_n +=1
    elif cmd == 2:
        new_n += 2
    elif cmd == 3:
        new_n *= 3
    
        
    if new_n == 9:
        is_nine = True

    if new_n == 12:
        return 0

    if new_n == 19:
        if is_nine:
            return 1
        else:
            return 0
    elif new_n < 19:
        lcntr = 0
        lcntr += F(new_n, 1, is_nine)
        lcntr += F(new_n, 2, is_nine)
        lcntr += F(new_n, 3, is_nine)
        return lcntr
    elif new_n > 19:
        return 0
        
print(F(2, 0, False))

