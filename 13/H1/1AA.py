# mask 255.255.?.0
# 10010110 - 150
# 11001000 - 200
# mask - 10000000 - 128

# mask 255.255.128.0

cntr = 0

for i in range(128,256):
    for j in range(0,256):
        cntr_1 = bin(161).count("1") + bin(137).count("1")
        
        cntr_1 += bin(i).count("1")
        cntr_1 += bin(j).count("1")
        
        if cntr_1 % 2 == 0:
            cntr +=1
            
print(cntr)