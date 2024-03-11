def calc(n):
    binary = bin(n)[2:]
    if(len(binary) != 8):
        binary = "0"*(8-len(binary)) + binary
    
    new_bin = "".join(["1" if x == "0" else "0" for x in binary])
    new_dec = int(new_bin, 2)
    return new_dec - n

for N in range(256):
    if(calc(N) == 111):
        print(N)