
def alg(s: str):
    while "4444" in s or "844" in s or "84" in s:
        if "4444" in s:
            s = s.replace("4444", "884", 1)
        if "844" in s:
            s = s.replace("844", "488", 1)
        if "84" in s:
            s = s.replace("84", "3343", 1)

    return s

for n in range(4, 10000):
    s = "8"+(n*"4")
    s2 = alg(s)
    if len(s2) >= 20:
        print(n)


# Не учел строку где написанно что n>=N типа что после этого числа все остальные тоже должны давать >= 20
