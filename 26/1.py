f = open('26_1.txt')
kol = f.readline()
k = f.readlines()
n = list(map(int, k))
m = 0
s = 0
c = 0
ns = set(n)
for i in range(1, len(n) - 1):
    for j in range(i + 1, len(n)):
        if n[i] % 2 != 0 and n[j] % 2 != 0:
            s = (n[i] + n[j]) // 2
            if s in ns:
                c += 1
                if s > m:
                    m = s
print(c, m)