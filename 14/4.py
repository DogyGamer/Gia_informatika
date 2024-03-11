import math
val = 49**7 + 7**21 - 7
val1 = 49**7 + 7**21 - 7
res = ""
val_arr = val

while val > 0:
    res = str(val % 7) + res
    val //= 7


str_res = "".join(map(str, res))
print("".join(map(str, res)), int(str_res, 7) - val1)

print(str_res.count("6"))