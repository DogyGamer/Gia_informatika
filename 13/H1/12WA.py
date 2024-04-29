cntr = 0
for third_octet in range(64,128):
    for fourth_octet in range(1,255):
        octets = [216, 130,third_octet,fourth_octet]
        if all([x % 2 == 0 for x in octets]):
            cntr += 1
            
print(cntr) # - 4064
