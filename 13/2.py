ip  = "224.24.254.134".split(".")
mask = "255.255.224.0".split(".")

def retrive(string):
    return (8-len(string))*"0"+string

for i in range(len(mask)):
    ip_seg = list(map(int, retrive(bin(int(ip[i]))[2:])))
    mask_seg = list(map(int, retrive(bin(int(mask[i]))[2:])))
    res = []
    for j in range(len(ip_seg)):
        res.append(ip_seg[j] and mask_seg[j])
    
    print(int("".join(map(str, res)), 2))   