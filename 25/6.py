base = 4891
i = 1
while i*base < 10**10:
    val = str(i*base)
    if val[-1] == "0" and val[0] == "1" and val[2:6] == "2711":
        print(val)
    i += 1
    
print("Done")


# ANS
# 1027110
# 10271100
# 102711000
# 1027110000
# 1527116930