def F(N):
    binary = list(map(int, bin(N)[2:]))
    binary.append(sum(binary)%2)
    binary.append(sum(binary)%2)
    return int("".join(map(str, binary)), 2)

for i in range(1000000):
    if F(i) > 97:
        print(F(i), i)
        break


    
    