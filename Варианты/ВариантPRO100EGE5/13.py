import ipaddress

net = ipaddress.ip_network("136.36.240.16/255.255.255.248")

cntr = 0

for ip in net.hosts():
    if "101" in bin(int(str(ip).split(".")[3])):
        continue
    else:
        cntr +=1
        print(bin(int(ip)), ip)
        
print(cntr)