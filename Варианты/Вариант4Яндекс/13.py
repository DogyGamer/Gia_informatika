import ipaddress

net1 = ipaddress.ip_network("192.168.56.192/255.255.255.192")
net2 = ipaddress.ip_network("192.168.56.208/255.255.255.240")

ips1 = [int(ip) for ip in net1.hosts()]
ips2 = [int(ip) for ip in net2.hosts()]

print(len(ips1), len(ips2))


cntr = 0

for ip in ips1:
    if ip in ips2:
        cntr += 1
        
for ip in ips2:
    if ip in ips1:
        cntr += 1
        
print(len(ips2)+len(ips1)-cntr)