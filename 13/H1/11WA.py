
cntr = 0
for octet2 in range(32, 64):
    for octet3 in range(0,255):
        for octet4 in range(1,255):
            octets = [117, octet2, octet3, octet4]
            if len(set(octets)) == 3:
                cntr += 1
                
print(cntr) # - 40384

# 11100000 - 224
# 00100000 - 32

# 111111