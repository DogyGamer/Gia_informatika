import ipaddress

net = ipaddress.ip_network("195.102.65.64/255.255.255.192")

cntr = 0
for ip in net:
    octet = "0"+bin(int(str(ip).split(".")[-1]))[2:]
    print(octet)
    if octet.count("0") == octet.count("1"):
        cntr += 1
        
print(cntr) #20