import ipaddress

net = ipaddress.ip_network("114.179.203.128/255.255.255.192")

cntr = 0

for ip in net.hosts():
    c = bin(int(ip))[2:].count("1")
    if c % 3 == 0:
        cntr += 1
        
print(cntr)