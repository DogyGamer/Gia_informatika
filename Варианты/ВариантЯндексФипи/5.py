def R(n):
    n2 = bin(n)[2:]
    if n % 3 == 0:
        r = n2 + n2[-1:-4:-1][::-1] 
    else:
        r = n2 + bin((n % 3)*3)[2:]
    return int("".join(r),2)



for i in range(4,100):
    r = R(i)
    if r < 76:
        print(i, r)