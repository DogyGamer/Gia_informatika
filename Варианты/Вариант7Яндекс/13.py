import ipaddress

net = ipaddress.ip_network("95.112.224.0/255.255.255.128")

ts = lambda x: "".join(list(map(str, x)))


cntr = 0
for ip in net.hosts():
    a = bin(int(str(ip).split(".")[-1]))[2:]
    b =  "".join(list(map(str, a)))
    if len(b) < 8:
        b = "0"*(8-len(b)) + b
    # print(b)
    if ts(b) == ts(reversed(b)):
        print(b)
        cntr += 1
        
print(cntr)