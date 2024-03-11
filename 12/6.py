
def alg(str):
    while "111" in str or "66" in str:
        if "6666" in str:
            str = str.replace("6666", "1", 1)
        else:
            str = str.replace("111", "3", 1)
        
        if "66" in str:
            str = str.replace("66", "6", 1)

    return str


for n in range(4,1_000+1):
    str = "1"+"6"*n
    
    res = alg(str)
    if res.count("3") >= 5:
        print(n)