import ipaddress
# for i in range(0, 256):
#     net = ipaddress.ip_network(f"183.192.{str(i)}.0/255.255.252.0")
    
#     if all([str(x).split(".")[2].count("1")+str(x).split(".")[3].count("1") > 3 for x in net.hosts()]):
#         print(i)
        
net = ipaddress.ip_network(f"183.192.28.0/255.255.252.0")
    
res = []
for host in net.hosts():
    shs = str(host).split(".")
    cnt = bin(int(shs[2])).count("1") + bin(int(shs[3])).count("1")
    res.append(cnt > 3)

print(all(res))