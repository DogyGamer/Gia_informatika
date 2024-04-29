# 99.165.134.0 - net addr.
# 255.255.254.0 - mask
# ones count more than three
cntr = 0
for j in [134,135]:
    for i in range(0, 256):
        ones_cnt = bin(j).count("1") + bin(i).count("1") + bin(99).count("1") + bin(165).count("1")
        if ones_cnt % 3 == 0:
            cntr += 1
        
print(cntr)