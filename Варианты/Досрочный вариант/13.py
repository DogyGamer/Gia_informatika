import ipaddress


net = ipaddress.ip_network("105.224.200.0/255.255.255.224")

cntr = 0

for ip in net.hosts():
    a = int(ip)
    b = "".join(bin(a)[2:])
    if b.count("1") % 4 == 0:
        cntr += 1
        
print(cntr)