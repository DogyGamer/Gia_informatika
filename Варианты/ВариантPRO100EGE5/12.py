
def alg(s:str):
    while "52" in s or "2222" in s or "1122" in s:
        if "52" in s:
            s = s.replace("52", "11", 1)
        if "2222" in s:
            s = s.replace("2222", "5", 1)
        if "1122" in s:
            s = s.replace("1122", "25", 1)
    return s


for n in range(4, 10_000):
    st = "5"+n*"2"
    res = list(map(int, alg(st)))
    if str(sum(res))[-1] == "7":
        print(n)
        break