import ipaddress

net = ipaddress.ip_network("154.63.0.0/255.255.0.0")

cntr = 0

for ip in net.hosts():
    print(ip)
    if bin(int(ip))[2:].count("1") % 2 == 0:
        cntr += 1

# 154.63.0.0 
# 154.63.255.255

print(cntr)
    
    
# 00100100 - 100
# 11001110 - 206
# 00000000 - 0

# 10000001 -129
# 01001011 -75 
# 00000000 -0

# 11000000
# 11001110
# 11111000 - 248