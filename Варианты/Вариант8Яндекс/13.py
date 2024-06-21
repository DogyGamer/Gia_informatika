import ipaddress

net = ipaddress.ip_network("242.128.0.0/255.192.0.0")

print(net.broadcast_address)

# 224

# 11110010.10111110.11000100.10 011111
# 11111111.11111111.11111111.11 000000
# 11110010.10111110.11000100.10 111111
