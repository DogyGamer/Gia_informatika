mask = 240
net = 160

cntr = 0

for i in range(161, 255):
    if i & mask == 160:
        if i % 2 == 0 and bin(i)[2:].count("1") % 2 == 0:
            cntr += 1
            
print(cntr)

# Учел адрес сети, хотя не должен был....

