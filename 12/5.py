
def alg(stri):
    while "52" in stri or "2222" in stri or "1112" in stri:
        if "52" in stri:
            stri = stri.replace("52", "11", 1)
            stri = stri.replace("2222", "5", 1)
        else:
            stri = stri.replace("1112", "2", 1)
    
    return stri

for n in range(3, 10_000+1):
    stri = "5"+"2"*n
    
    res = alg(stri)
    if sum(map(int, res)) == 1685:
        print(n)