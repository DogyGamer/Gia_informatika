maskcntr = (bin(255).count("1")*2)+bin(224).count("1")

import ipaddress

net = ipaddress.ip_network("192.168.160.0/255.255.224.0")

cntr = 0

for ip in net.hosts():
    if bin(int(ip)).count("1") == maskcntr:
        cntr += 1
        
print(cntr)